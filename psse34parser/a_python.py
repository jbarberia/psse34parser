import psse34
import psspy
import psse34parser
import sliderPy
import os
import re

def format_value(val, default=None):
    """Dado un valor formatearlo para que quede bien en el codigo

    Args:
        val: Valor a convertir
        default (optional): En caso de que `val` sea `None` devuelve el valor por defecto. Defaults to None.

    Returns:
        str: Valor en el formato adecuado
    """
    if isinstance(val, int):
        return val
    elif isinstance(val, float):
        return round(val, 8)
    elif isinstance(val, str):
        return "'{}'".format(val)
    else:
        return default


def crea_codigo(raw, seq):
    """Para cada seccion de elementos en el RAW y SEQ crea las lineas de codigo necesarias para replicarlo
    hasta el momento solo es posible generar:
        - Buses
        - Loads
        - Fixed Shunts
        - Generators
        - Non transformer Branch
        - Switching Devices
        - Transformer (2W y 3W)
        - Switched Shunts
    Hay que aclarar que no genera AREAS, ZONAS ni OWNERS.

    Args:
        raw (dict): Diccionario con el mapeo del RAW
        seq (dict): Diccionario con el mapeo del SEQ

    Returns:
        str: Codigo a ejecutar
    """
    codigo = []

    # BUSES
    codigo.append("\n# Barras")
    codigo.append("# ------")
    for bus_dict in raw["BUS"]:
        ibus = bus_dict["I"]
        name = format_value(bus_dict["NAME"])
        inode = 0

        intgar = [
            bus_dict["IDE"],
            bus_dict["AREA"],
            bus_dict["ZONE"],
            bus_dict["OWNER"],
        ]

        realar = [
            bus_dict["BASKV"],
            bus_dict["VM"],
            bus_dict["VA"],
            bus_dict["NVHI"],
            bus_dict["NVLO"],
            bus_dict["EVHI"],
            bus_dict["EVLO"],
        ]

        # codigo.append("# Barra {} {}".format(ibus, name))
        codigo.append(
            "psspy.bus_data_4({}, {}, {}, {}, {})".format(ibus, inode, intgar, realar, name)
        )
    

    # LOADS
    loads_raw = {(load["I"], load["ID"]): load for load in raw["LOAD"]}
    loads_seq = {(load["I"], load["ID"]): load for load in seq["LOAD"]}

    loads = loads_raw
    for key, dict_value in loads.items():
        dict_value.update(loads_seq.get(key, {}))
    
    if loads:
        codigo.append("\n# Demandas")
        codigo.append("# --------")
    for key, load_dict in loads.items():
        ibus = load_dict["I"]
        id = format_value(load_dict["ID"])

        intgar = [
            load_dict["STAT"],
            load_dict["AREA"],
            load_dict["ZONE"],
            load_dict["OWNER"],
            load_dict["SCALE"],
            load_dict["INTRPT"],
            load_dict["DGENF"],
        ]

        realar = [
            load_dict["PL"],
            load_dict["QL"],
            load_dict["IP"],
            load_dict["IQ"],
            load_dict["YP"],
            load_dict["YQ"],
            load_dict["DGENP"],
            load_dict["DGENQ"],
        ]

        # codigo.append("# Demanda {} {}".format(ibus, id))
        codigo.append(
            "psspy.load_data_5({}, {}, {}, {})".format(
                ibus, id, intgar, realar
            )
        )

        intgar = [
            load_dict.get("GRDFLG", 0)
        ]

        realar = [
            load_dict.get("PNEG", 0.0),
            load_dict.get("QNEG", 0.0),
            load_dict.get("PZERO", 0.0),
            load_dict.get("QZERO", 0.0),
        ]

        codigo.append(
            "psspy.seq_load_data({}, {}, {}, {})".format(
                ibus, id, intgar, realar
            )
        )

    # FIXED SHUNT
    fshunt_raw = {(fsh["I"], fsh["ID"]): fsh for fsh in raw["FIXED SHUNT"]}
    fshunt_seq = {(fsh["I"], fsh["ID"]): fsh for fsh in seq["ZERO SEQ. FIXED SHUNT"]}

    fshunt = fshunt_raw
    for key, dict_value in fshunt.items():
        dict_value.update(fshunt_seq.get(key, {}))

    if fshunt:
        codigo.append("\n# Fixed Shunts")
        codigo.append("# ------------")
    for key, fshunt_dict in fshunt.items():
        ibus = fshunt_dict["I"]
        id = format_value(fshunt_dict["ID"])

        intgar = [
            fshunt_dict["STATUS"],
        ]
        
        realar = [
            fshunt_dict["GL"],
            fshunt_dict["BL"],
        ]

        codigo.append(
            "psspy.shunt_data({}, {}, {}, {})".format(ibus, id, intgar, realar)
        )

        realar = [
            fshunt_dict.get("GSZERO", 0.0),
            fshunt_dict.get("BSZERO", 0.0),
        ]

        codigo.append(
            "psspy.seq_fixed_shunt_data({}, {}, {})".format(ibus, id, realar)
        )


    # GENERADORES
    generators_raw = {(gen["I"], gen["ID"]): gen for gen in raw["GENERATOR"]}
    generators_seq = {(gen["I"], gen["ID"]): gen for gen in seq["GENERATOR"]}
    ncsfc = {(gen["I"], gen["ID"]): gen for gen in seq["NON CONVENTIONAL SOURCE FAULT CONTRIBUTION"]}

    generators = generators_raw
    for key, dict_value in generators.items():
        dict_value.update(generators_seq.get(key, {}))
    
    if generators:
        codigo.append("\n# Generadores")
        codigo.append("# -----------")
    for key, gen_dict in generators.items():
        ibus = gen_dict["I"]
        id = format_value(gen_dict["ID"])
                
        intgar = [
            gen_dict["IREG"]
        ]
        
        realar = [
            gen_dict["VS"],
            gen_dict["RMPCT"],
        ]

        codigo.append("psspy.plant_data({}, {}, {})".format(ibus, intgar, realar))

        intgar = [
            gen_dict["STAT"],
            gen_dict["O1"],
            gen_dict["O2"],
            gen_dict["O3"],
            gen_dict["O4"],
            gen_dict["WMOD"],
        ]
        intgar = [format_value(x, 0) for x in intgar]
        
        realar = [
            gen_dict["PG"],
            gen_dict["QG"],
            gen_dict["QT"],
            gen_dict["QB"],
            gen_dict["PT"],
            gen_dict["PB"],
            gen_dict["MBASE"],
            gen_dict["ZR"],
            gen_dict["ZX"],
            gen_dict["RT"],
            gen_dict["XT"],
            gen_dict["GTAP"],
            gen_dict["F1"],
            gen_dict["F2"],
            gen_dict["F3"],
            gen_dict["F4"],
            gen_dict["WPF"],
        ]
        realar = [format_value(x, 1.0) for x in realar]
        
        codigo.append(
            "psspy.machine_data_2({}, {}, {}, {})".format(
                ibus, id, intgar, realar
            )
        )

        intgar = [
            gen_dict["CZG"],
        ]
        
        realar = [
            gen_dict["ZRPOS"],
            gen_dict["ZXPPDV"],
            gen_dict["ZRNEG"],
            gen_dict["ZXNEGDV"],
            gen_dict["ZR0"],
            gen_dict["ZX0DV"],
            gen_dict["ZXPDV"],
            gen_dict["ZXSDV"],
            gen_dict["ZRG"],
            gen_dict["ZXG"],
            gen_dict["REFDEG"],
        ]
        
        codigo.append(
            "psspy.seq_machine_data_4({}, {}, {}, {})".format(
                ibus, id, intgar, realar
            )
        )

        if key in ncsfc:
            ncsfc_dict = ncsfc[key]

            points = 6
            t = []
            p = []
            q = []
            for i in range(1, points + 1):
                t.append(ncsfc_dict["T{}".format(i)])
                p.append(ncsfc_dict["C{}P".format(i)])
                q.append(ncsfc_dict["C{}Q".format(i)])
            
            t = [x for x in t if x != 'None' and x != None]
            p = [x for x in p if x != 'None' and x != None]
            q = [x for x in q if x != 'None' and x != None]

            points = len(t)
            realar = t
            cplxar = [p_i + q_i * 1j for p_i, q_i in zip(p, q)]

            codigo.append(
                "psspy.seq_ncs_flt_cntrb_data({}, {}, {}, {}, {})".format(
                    ibus, id, points, realar, cplxar
                    )
                )


    # BRANCH
    brn_raw = {(br["I"], br["J"], br["CKT"]): br for br in raw["BRANCH"]}     
    brn_seq = {(br["I"], br["J"], br["ICKT"]): br for br in seq["ZERO SEQ. NON-TRANSFORMER BRANCH"]}     
    brn = brn_raw
    for key, dict_value in brn.items():
        dict_value.update(brn_seq.get(key, {}))
    
    if brn:
        codigo.append("\n# Lineas")
        codigo.append("# ------")
    for key, brn_dict in brn.items():
        ibus = brn_dict["I"]
        jbus = brn_dict["J"]
        ckt = format_value(brn_dict["CKT"])

        intgar = [
            brn_dict["STAT"],
            brn_dict["MET"],
            brn_dict["O1"],
            brn_dict["O2"],
            brn_dict["O3"],
            brn_dict["O4"],
        ]
        intgar = [format_value(x, 0) for x in intgar]

        realar = [
            brn_dict["R"],
            brn_dict["X"],
            brn_dict["B"],
            brn_dict["GI"],
            brn_dict["BI"],
            brn_dict["GJ"],
            brn_dict["BJ"],
            brn_dict["LEN"],
            brn_dict["F1"],
            brn_dict["F2"],
            brn_dict["F3"],
            brn_dict["F4"],
        ]
        realar = [format_value(x, 0) for x in realar]

        ratings = [
            brn_dict["RATE1"],
            brn_dict["RATE2"],
            brn_dict["RATE3"],
            brn_dict["RATE4"],
            brn_dict["RATE5"],
            brn_dict["RATE6"],
            brn_dict["RATE7"],
            brn_dict["RATE8"],
            brn_dict["RATE9"],
            brn_dict["RATE10"],
            brn_dict["RATE11"],
            brn_dict["RATE12"],
        ]

        namear = format_value(brn_dict["NAME"])
        codigo.append(
            "psspy.branch_data_3({}, {}, {}, {}, {}, {}, {})".format(ibus, jbus, ckt, intgar, realar, ratings, namear)
        )

        intgar = [
            brn_dict.get("SCTYP", 0)
        ]
        
        realar = [
            brn_dict.get("RLINZ", 0.0),
            brn_dict.get("XLINZ", 0.0),
            brn_dict.get("BCHZ", 0.0),
            brn_dict.get("GI", 0.0),
            brn_dict.get("BI", 0.0),
            brn_dict.get("GJ", 0.0),
            brn_dict.get("BJ", 0.0),
            brn_dict.get("IPR", 0.0),
        ]

        codigo.append(
            "psspy.seq_branch_data_3({}, {}, {}, {}, {})".format(ibus, jbus, ckt, intgar, realar)
        )


    # SYSTEM SWITCHING DEVICE
    if raw["SYSTEM SWITCHING DEVICE"]:
        codigo.append("\n# Interruptores")
        codigo.append("# -------------")
    for swd in raw["SYSTEM SWITCHING DEVICE"]:
        ibus = swd["I"]
        jbus = swd["J"]
        ckt = format_value(swd["CKT"])
        intgar = [
            swd["STAT"],
            swd["NSTAT"],
            swd["MET"],
            swd["STYPE"],
        ]
        
        rbrxar = swd["X"]
        
        realar = [
            swd["RATE1"],
            swd["RATE2"],
            swd["RATE3"],
            swd["RATE4"],
            swd["RATE5"],
            swd["RATE6"],
            swd["RATE7"],
            swd["RATE8"],
            swd["RATE9"],
            swd["RATE10"],
            swd["RATE11"],
            swd["RATE12"],
        ]
        
        namear = format_value(swd["NAME"])
        
        codigo.append(
            "psspy.system_swd_data({}, {}, {}, {}, {}, {}, {})".format(ibus, jbus, ckt, intgar, rbrxar, realar, namear)
        )


    # 2W TRANSFORMER
    trn_raw = {(trn[0]["I"], trn[0]["J"], trn[0]["K"], trn[0]["CKT"]): trn for trn in raw["TRANSFORMER"]}     
    trn_seq = {(trn["I"], trn["J"], trn["K"], trn["ICKT"]): trn for trn in seq["ZERO SEQ. TRANSFORMER"]}  

    trn = trn_raw
    for key, dict_value in trn.items():
        if key[2] == 0: # 2W
            if key in trn_seq.keys():
                dict_value.append(trn_seq.get(key, {}))

            new_key = key[1], key[0], key[2], key[3]
            if new_key in trn_seq.keys():
                dict_value.append(trn_seq.get(new_key, {}))

        else: # 3W
            dict_value.append(trn_seq.get(key, {}))
    
    if trn:
        codigo.append("\n# Transformadores")
        codigo.append("# ---------------")
    for key, trn_dict in trn.items():
        ibus = trn_dict[0]["I"]
        jbus = trn_dict[0]["J"]
        kbus = trn_dict[0]["K"]
        ckt = format_value(trn_dict[0]["CKT"])

        if kbus == 0: # 2W

            intgar = [
                trn_dict[0]["STAT"],
                ibus if trn_dict[0]["NMETR"] != 1 else jbus,
                trn_dict[0]["O1"],
                trn_dict[0]["O2"],
                trn_dict[0]["O3"],
                trn_dict[0]["O4"],
                trn_dict[2]["NTP1"],
                trn_dict[2]["TAB1"],
                ibus,
                trn_dict[2]["CONT1"],
                trn_dict[2].get("NODE1", 0),
                1, # NO SE QUE PONER PARA SICOD1
                trn_dict[2]["COD1"],
                trn_dict[0]["CW"],
                trn_dict[0]["CZ"],
                trn_dict[0]["CM"],
            ]

            realar = [
                trn_dict[1]["R1-2"],
                trn_dict[1]["X1-2"],
                trn_dict[1]["SBASE1-2"],
                trn_dict[2]["WINDV1"],
                trn_dict[2]["NOMV1"],
                trn_dict[2]["ANG1"],
                trn_dict[3]["WINDV2"],
                trn_dict[3]["NOMV2"],
                trn_dict[0]["F1"],
                trn_dict[0]["F2"],
                trn_dict[0]["F3"],
                trn_dict[0]["F4"],
                trn_dict[0]["MAG1"],
                trn_dict[0]["MAG2"],
                trn_dict[2]["RMA1"],
                trn_dict[2]["RMI1"],
                trn_dict[2]["VMA1"],
                trn_dict[2]["VMI1"],
                trn_dict[2]["CR1"],
                trn_dict[2]["CX1"],
                trn_dict[2]["CNXA1"],
            ]

            ratings = [
                trn_dict[2]["RATE1-1"],
                trn_dict[2]["RATE1-2"],
                trn_dict[2]["RATE1-3"],
                trn_dict[2]["RATE1-4"],
                trn_dict[2]["RATE1-5"],
                trn_dict[2]["RATE1-6"],
                trn_dict[2]["RATE1-7"],
                trn_dict[2]["RATE1-8"],
                trn_dict[2]["RATE1-9"],
                trn_dict[2]["RATE1-10"],
                trn_dict[2]["RATE1-11"],
                trn_dict[2]["RATE1-12"],
            ]

            namear = format_value(trn_dict[0]["NAME"])
            vgrpar = format_value(trn_dict[0]["VECGRP"])
            
            codigo.append(
                "psspy.two_winding_data_6({}, {}, {}, {}, {}, {}, {})".format(ibus, jbus, ckt, intgar, realar, ratings, namear, vgrpar)
            )

            intgar = [
                trn_dict[-1]["CC"],
                trn_dict[-1]["CZ0"],
                trn_dict[-1]["CZG"],
            ]

            realar = [
                trn_dict[-1]["RG1"],
                trn_dict[-1]["XG1"],
                trn_dict[-1]["R01"],
                trn_dict[-1]["X01"],
                trn_dict[-1]["RG2"],
                trn_dict[-1]["XG2"],
                trn_dict[-1]["R02"],
                trn_dict[-1]["X02"],
                trn_dict[-1]["RNUTRL"],
                trn_dict[-1]["XNUTRL"],
            ]

            codigo.append(
                "psspy.seq_two_winding_data_3({}, {}, {}, {}, {})\n".format(ibus, jbus, ckt, intgar, realar)
            )


        else: # 3W
            
            intgar = [
                trn_dict[0]["O1"],
                trn_dict[0]["O2"],
                trn_dict[0]["O3"],
                trn_dict[0]["O4"],
                trn_dict[0]["CW"],
                trn_dict[0]["CZ"],
                trn_dict[0]["CM"],
                trn_dict[0]["STAT"],
                trn_dict[0]["NMETR"],
                trn_dict[0]["I"],
                trn_dict[0]["J"],
                trn_dict[0]["K"],
            ]

            realar = [
                trn_dict[1]["R1-2"],
                trn_dict[1]["X1-2"],
                trn_dict[1]["R2-3"],
                trn_dict[1]["X2-3"],
                trn_dict[1]["R3-1"],
                trn_dict[1]["X3-1"],
                trn_dict[1]["SBASE1-2"],
                trn_dict[1]["SBASE2-3"],
                trn_dict[1]["SBASE3-1"],
                trn_dict[0]["MAG1"],
                trn_dict[0]["MAG2"],
                trn_dict[0]["F1"],
                trn_dict[0]["F2"],
                trn_dict[0]["F3"],
                trn_dict[0]["F4"],
                trn_dict[1]["VMSTAR"],
                trn_dict[1]["ANSTAR"],
            ]

            name = format_value(trn_dict[0]["NAME"])

            codigo.append(
                "psspy.three_wnd_imped_data_4({}, {}, {}, {}, {}, {}, {})".format(ibus, jbus, kbus, ckt, intgar, realar, name)
            )
            

            for i in range(2, 5):
                wnd = i - 1

                intgar = [
                    trn_dict[i]["NTP{}".format(wnd)],
                    trn_dict[i]["TAB{}".format(wnd)],
                    trn_dict[i]["CONT{}".format(wnd)],
                    trn_dict[i]["NOD{}".format(wnd)],
                    1,
                    trn_dict[i]["COD{}".format(wnd)],
                ]

                realar = [
                    trn_dict[i]["WINDV{}".format(wnd)],
                    trn_dict[i]["NOMV{}".format(wnd)],
                    trn_dict[i]["ANG{}".format(wnd)],
                    trn_dict[i]["RMA{}".format(wnd)],
                    trn_dict[i]["RMI{}".format(wnd)],
                    trn_dict[i]["VMA{}".format(wnd)],
                    trn_dict[i]["VMI{}".format(wnd)],
                    trn_dict[i]["CR{}".format(wnd)],
                    trn_dict[i]["CX{}".format(wnd)],
                    trn_dict[i]["CNXA{}".format(wnd)],
                ]

                ratings = [
                    trn_dict[i]["RATE{}-1".format(wnd)],
                    trn_dict[i]["RATE{}-2".format(wnd)],
                    trn_dict[i]["RATE{}-3".format(wnd)],
                    trn_dict[i]["RATE{}-4".format(wnd)],
                    trn_dict[i]["RATE{}-5".format(wnd)],
                    trn_dict[i]["RATE{}-6".format(wnd)],
                    trn_dict[i]["RATE{}-7".format(wnd)],
                    trn_dict[i]["RATE{}-8".format(wnd)],
                    trn_dict[i]["RATE{}-9".format(wnd)],
                    trn_dict[i]["RATE{}-10".format(wnd)],
                    trn_dict[i]["RATE{}-11".format(wnd)],
                    trn_dict[i]["RATE{}-12".format(wnd)],
                ]

                codigo.append(
                    "psspy.three_wnd_winding_data_5({}, {}, {}, {}, {}, {}, {}, {})".format(ibus, jbus, kbus, ckt, wnd, intgar, realar, ratings)
                )
                

            intgar = [
                trn_dict[-1]["CZ0"], 
                trn_dict[-1]["CZG"], 
                trn_dict[-1]["CC"], 
            ]

            realar = [
                trn_dict[-1]["RG1"],
                trn_dict[-1]["XG1"],
                trn_dict[-1]["R01"],
                trn_dict[-1]["X01"],
                trn_dict[-1]["RG2"],
                trn_dict[-1]["XG2"],
                trn_dict[-1]["R02"],
                trn_dict[-1]["X02"],
                trn_dict[-1]["RG3"],
                trn_dict[-1]["XG3"],
                trn_dict[-1]["R03"],
                trn_dict[-1]["X03"],
                trn_dict[-1]["RNUTRL"],
                trn_dict[-1]["XNUTRL"],
            ]

            codigo.append(
                "psspy.seq_three_winding_data_3({}, {}, {}, {}, {}, {})\n".format(ibus, jbus, kbus, ckt, intgar, realar)
            )


    # SWITCHED SHUNTS
    sshunt_raw = {sh["I"]: sh for sh in raw["SWITCHED SHUNT"]}
    sshunt_seq = {sh["I"]: sh for sh in seq["ZERO SEQ. SWITCHED SHUNT"]}

    sshunt = sshunt_raw
    for key, dict_value in sshunt.items():
        dict_value.update(sshunt_seq.get(key, {}))

    if sshunt:
        codigo.append("\n# Switched Shunts")
        codigo.append("# ---------------")
    for key, shunt_dict in sshunt.items():
        ibus = shunt_dict["I"]

        intgar = [
            shunt_dict["N1"],
            shunt_dict["N2"],
            shunt_dict["N3"],
            shunt_dict["N4"],
            shunt_dict["N5"],
            shunt_dict["N6"],
            shunt_dict["N7"],
            shunt_dict["N8"],
            shunt_dict["MODSW"],
            shunt_dict["SWREG"],
            shunt_dict["NREG"],
            shunt_dict["ST"],
            shunt_dict["ADJM"],
        ]
        intgar = [format_value(x, 0) for x in intgar]

        realar = [
            shunt_dict["B1"],
            shunt_dict["B2"],
            shunt_dict["B3"],
            shunt_dict["B4"],
            shunt_dict["B5"],
            shunt_dict["B6"],
            shunt_dict["B7"],
            shunt_dict["B8"],        
            shunt_dict["VSWHI"],        
            shunt_dict["VSWLO"],        
            shunt_dict["BINIT"],        
            shunt_dict["RMPCT"],        
        ]
        realar = [format_value(x, 0.0) for x in realar]

        codigo.append(
            "psspy.switched_shunt_data_4({}, {}, {})".format(
                ibus, intgar, realar, 
            )
        )

        realar = [
            shunt_dict["BZ1"],
            shunt_dict["BZ2"],
            shunt_dict["BZ3"],
            shunt_dict["BZ4"],
            shunt_dict["BZ5"],
            shunt_dict["BZ6"],
            shunt_dict["BZ7"],
            shunt_dict["BZ8"], 
        ]
        realar = [format_value(x, 0.0) for x in realar]

        codigo.append(
            "psspy.seq_switched_shunt_data({}, {})".format(
                ibus, realar, 
            )
        )

    return "\n".join(codigo)
