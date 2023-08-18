# Keys of the data dict data
HEADERKEYS = ["IC", "SBASE", "REV", "XFRRAT", "NXFRAT", "BASFRQ"]
BUSKEYS = ["I", "NAME", "BASKV", "IDE", "AREA", "ZONE", "OWNER", "VM", "VA", "NVHI", "NVLO", "EVHI", "EVLO"]
LOADKEYS = ["I", "ID", "STAT", "AREA", "ZONE", "PL", "QL", "IP", "IQ", "YP", "YQ", "OWNER", "SCALE", "INTRPT", "DGENP", "DGENQ", "DGENF"]
FIXEDSHUNTKEYS = ["I", "ID", "STATUS", "GL", "BL"]
GENERATORKEYS = [ "I", "ID", "PG", "QG", "QT", "QB", "VS","IREG", "MBASE", "ZR", "ZX", "RT", "XT", "GTAP","STAT", "RMPCT", "PT", "PB", "O1", "F1", "O2", "F2", "O3", "F3","O4", "F4", "WMOD", "WPF", "NREG"]
BRANCHKEYS = ["I", "J", "CKT", "R", "X", "B", "NAME", "RATE1", "RATE2", "RATE3", "RATE4", "RATE5", "RATE6", "RATE7", "RATE8", "RATE9", "RATE10", "RATE11", "RATE12", "GI", "BI", "GJ", "BJ", "STAT", "MET", "LEN", "O1", "F1", "O2", "F2", "O3", "F3", "O4", "F4"]
SYSTEMSWITCHINGDEVICEKEYS = ["I", "J", "CKT", "X", "RATE1", "RATE2", "RATE3", "RATE4", "RATE5", "RATE6", "RATE7", "RATE8", "RATE9", "RATE10", "RATE11", "RATE12", "STAT", "NSTAT", "MET", "STYPE", "NAME"]
TRANSFORMERP1KEYS=["I", "J", "K", "CKT", "CW", "CZ", "CM", "MAG1", "MAG2", "NMETR", "NAME", "STAT", "O1", "F1", "O2", "F2", "O3", "F3", "O4", "F4", "VECGRP", "ZCOD"]
TRANSFORMERP2KEYS = ["R1-2", "X1-2", "SBASE1-2", "R2-3", "X2-3", "SBASE2-3", "R3-1", "X3-1", "SBASE3-1", "VMSTAR", "ANSTAR"]
TRANSFORMERL1KEYS = ["WINDV1", "NOMV1", "ANG1", "RATE1-1", "RATE1-2", "RATE1-3", "RATE1-4", "RATE1-5", "RATE1-6", "RATE1-7", "RATE1-8", "RATE1-9", "RATE1-10", "RATE1-11", "RATE1-12", "COD1", "CONT1", "RMA1", "RMI1", "VMA1", "VMI1", "NTP1", "TAB1", "CR1", "CX1", "CNXA1", "NOD1"]
TRANSFORMERL2KEYS = ["WINDV2", "NOMV2", "ANG2", "RATE2-1", "RATE2-2", "RATE2-3", "RATE2-4", "RATE2-5", "RATE2-6", "RATE2-7", "RATE2-8", "RATE2-9", "RATE2-10", "RATE2-11", "RATE2-12", "COD2", "CONT2", "RMA2", "RMI2", "VMA2", "VMI2", "NTP2", "TAB2", "CR2", "CX2", "CNXA2", "NOD2"]
TRANSFORMERL3KEYS = ["WINDV3", "NOMV3", "ANG3", "RATE3-1", "RATE3-2", "RATE3-3", "RATE3-4", "RATE3-5", "RATE3-6", "RATE3-7", "RATE3-8", "RATE3-9", "RATE3-10", "RATE3-11", "RATE3-12", "COD3", "CONT3", "RMA3", "RMI3", "VMA3", "VMI3", "NTP3", "TAB3", "CR3", "CX3", "CNXA3", "NOD3"]
AREAKEYS = ["I", "ISW", "PDES", "PTOL", "ARNAME"]
TWOTERMINALDCL1KEYS = ["NAME", "MDC", "RDC", "SETVL", "VSCHD", "VCMOD", "RCOMP", "DELTI", "METER", "DCVMIN", "CCCITMX", "CCCACC"]
TWOTERMINALDCL2KEYS = ["IPR", "NBR", "ANMXR", "ANMNR", "RCR", "XCR", "EBASR", "TRR", "TAPR", "TMXR", "TMNR", "STPR", "ICR", "IFR", "ITR", "IDR", "XCAPR", "NDR"]
TWOTERMINALDCL3KEYS=["IPI", "NBI", "ANMXI", "ANMNI", "RCI", "XCI", "EBASI", "TRI", "TAPI", "TMXI", "TMNI", "STPI", "ICI", "IFI", "ITI", "IDI", "XCAPI", "NDI"]
VSCDCLINEL1KEYS = ["NAME", "MDC", "RDC", "O1", "F1", "O2", "F2", "O3", "F3", "O4", "F4"]
VSCDCLINEL2KEYS = ["IBUS", "TYPE", "MODE", "DCSET", "ACSET", "ALOSS", "BLOSS", "MINLOSS", "SMAX", "IMAX", "PWF", "MAXQ", "MINQ", "VSREG", "RMPCT", "NREG"]
IMPEDANCECORRECTIONL1KEYS = ["I", "T1", "Re(F1)", "Im(F1)", "T2", "Re(F2)", "Im(F2)", "T3", "Re(F3)", "Im(F3)", "T4", "Re(F4)", "Im(F4)", "T5", "Re(F5)", "Im(F5)", "T6", "Re(F6)", "Im(F6)"]
IMPEDANCECORRECTIONL2KEYS = ["T7", "Re(F7)", "Im(F7)", "T8", "Re(F8)", "Im(F8)", "T9", "Re(F9)", "Im(F9)", "T10", "Re(F10)", "Im(F10)", "T11", "Re(F11)", "Im(F11)", "T12", "Re(F12)", "Im(F12)"]
MULTITERMINALDCL1KEYS = ["NAME","NCONV","NDCBS","NDCLN","MDC","VCONV","VCMOD","VCONVN"]
MULTITERMINALDCL2KEYS = ["IB", "N", "ANGMX", "ANGMN", "RC", "XC", "EBAS", "TR", "TAP", "TPMX", "TPMN", "TSTP", "SETVL", "DCPF", "MARG", "CNVCOD"]
MULTITERMINALDCL3KEYS = ["IDC","IB","AREA","ZONE","DCNAME","IDC2","RGRND","OWNER"]
MULTITERMINALDCL4KEYS = ["IDC","JDC","DCCKT","MET","RDC","LDC"]
MULTISECTIONLINEKEYS = ["I", "J", "'ID'", "MET", "DUM1", "DUM2", "DUM3", "DUM4", "DUM5", "DUM6", "DUM7", "DUM8", "DUM9"]
ZONEKEYS = ["I","ZONAME"]
INTERAREATRANSFERKEYS = ["ARFROM", "ARTO", "TRID", "PTRAN"]
OWNERKEYS = ["I", "OWNAME"]
FACTSKEYS = ["NAME","I","J","MODE","PDES","QDES","VSET","SHMX","TRMX","VTMN","VTMX","VSMX","IMX","LINX","RMPCT","OWNER","SET1","SET2","VSREF","FCREG","'MNAME'","NREG"]
SWITCHEDSHUNTKEYS = ["I", "MODSW", "ADJM", "ST", "VSWHI", "VSWLO", "SWREG", "RMPCT", "RMIDNT", "BINIT", "N1", "B1", "N2", "B2", "N3", "B3", "N4", "B4", "N5", "B5", "N6", "B6", "N7", "B7", "N8", "B8", "NREG"]
GNEKEYS = [] # Not supported yet
INDUCTIONMACHINEKEYS=["I", "'ID'", "ST", "SC", "DC", "AREA", "ZONE", "OWNER", "TC", "BC", "MBASE", "RATEKV", "PC", "PSET", "H", "A", "B", "D", "E", "RA", "XA", "XM", "R1", "X1", "R2", "X2", "X3", "E1", "SE1", "E2", "SE2", "IA1", "IA2", "XAMULT"]
SUBSTATIONKEYS = []

# Data type for each key
DTYPE_HEADERKEYS = {"IC": str, "SBASE": str, "REV": str, "XFRRAT": str, "NXFRAT": str, "BASFRQ": str}
DTYPE_BUSKEYS = {"I": int, "NAME": str, "BASKV": float, "IDE": int, "AREA": int, "ZONE": int, "OWNER": int, "VM": float, "VA": float, "NVHI": float, "NVLO": float, "EVHI": float, "EVLO": float}
DTYPE_LOADKEYS = {"I": int, "ID": str, "STAT": str, "AREA": str, "ZONE": str, "PL": str, "QL": str, "IP": str, "IQ": str, "YP": str, "YQ": str, "OWNER": str, "SCALE": str, "INTRPT": str, "DGENP": str, "DGENQ": str, "DGENF": str}
DTYPE_FIXEDSHUNTKEYS = {"I": str, "ID": str, "STATUS": str, "GL": str, "BL": str}
DTYPE_GENERATORKEYS = { "I": int, "ID": str, "PG": float, "QG": float, "QT": float, "QB": float, "VS": float,"IREG": float, "MBASE": float, "ZR": float, "ZX": float, "RT": float, "XT": float, "GTAP": float,"STAT": int, "RMPCT": float, "PT": float, "PB": float, "O1": int, "F1": float, "O2": int, "F2": float, "O3": int, "F3": float,"O4": int, "F4": float, "WMOD": int, "WPF": float, "NREG": str}
DTYPE_BRANCHKEYS = {"I": str, "J": str, "CKT": str, "R": str, "X": str, "B": str, "NAME": str, "RATE1": str, "RATE2": str, "RATE3": str, "RATE4": str, "RATE5": str, "RATE6": str, "RATE7": str, "RATE8": str, "RATE9": str, "RATE10": str, "RATE11": str, "RATE12": str, "GI": str, "BI": str, "GJ": str, "BJ": str, "STAT": str, "MET": str, "LEN": str, "O1": str, "F1": str, "O2": str, "F2": str, "O3": str, "F3": str, "O4": str, "F4": str}
DTYPE_SYSTEMSWITCHINGDEVICEKEYS = {"I": str, "J": str, "CKT": str, "X": str, "RATE1": str, "RATE2": str, "RATE3": str, "RATE4": str, "RATE5": str, "RATE6": str, "RATE7": str, "RATE8": str, "RATE9": str, "RATE10": str, "RATE11": str, "RATE12": str, "STAT": str, "NSTAT": str, "MET": str, "STYPE": str, "NAME": str}
DTYPE_TRANSFORMERP1KEYS={"I": int, "J": int, "K": int, "CKT": str, "CW": int, "CZ": int, "CM": int, "MAG1": float, "MAG2": float, "NMETR": int, "NAME": str, "STAT": int, "O1": int, "F1": float, "O2": int, "F2": float, "O3": int, "F3": float, "O4": int, "F4": float, "VECGRP": str, "ZCOD": int}
DTYPE_TRANSFORMERP2KEYS = {"R1-2": float, "X1-2": float, "SBASE1-2": float, "R2-3": float, "X2-3": float, "SBASE2-3": float, "R3-1": float, "X3-1": float, "SBASE3-1": float, "VMSTAR": float, "ANSTAR": float}
DTYPE_TRANSFORMERL1KEYS = {"WINDV1": float, "NOMV1": float, "ANG1": float, "RATE1-1": float, "RATE1-2": float, "RATE1-3": float, "RATE1-4": float, "RATE1-5": float, "RATE1-6": float, "RATE1-7": float, "RATE1-8": float, "RATE1-9": float, "RATE1-10": float, "RATE1-11": float, "RATE1-12": float, "COD1": int, "CONT1": int, "RMA1": float, "RMI1": float, "VMA1": float, "VMI1": float, "NTP1": int, "TAB1": int, "CR1": float, "CX1": float, "CNXA1": float, "NOD1": int}
DTYPE_TRANSFORMERL2KEYS = {"WINDV2": float, "NOMV2": float, "ANG2": float, "RATE2-1": float, "RATE2-2": float, "RATE2-3": float, "RATE2-4": float, "RATE2-5": float, "RATE2-6": float, "RATE2-7": float, "RATE2-8": float, "RATE2-9": float, "RATE2-10": float, "RATE2-11": float, "RATE2-12": float, "COD2": int, "CONT2": int, "RMA2": float, "RMI2": float, "VMA2": float, "VMI2": float, "NTP2": int, "TAB2": int, "CR2": float, "CX2": float, "CNXA2": float, "NOD2": int}
DTYPE_TRANSFORMERL3KEYS = {"WINDV3": float, "NOMV3": float, "ANG3": float, "RATE3-1": float, "RATE3-2": float, "RATE3-3": float, "RATE3-4": float, "RATE3-5": float, "RATE3-6": float, "RATE3-7": float, "RATE3-8": float, "RATE3-9": float, "RATE3-10": float, "RATE3-11": float, "RATE3-12": float, "COD3": int, "CONT3": int, "RMA3": float, "RMI3": float, "VMA3": float, "VMI3": float, "NTP3": int, "TAB3": int, "CR3": float, "CX3": float, "CNXA3": float, "NOD3": int}
DTYPE_AREAKEYS = {"I": str, "ISW": str, "PDES": str, "PTOL": str, "ARNAME": str}
DTYPE_TWOTERMINALDCL1KEYS = {"NAME": str, "MDC": str, "RDC": str, "SETVL": str, "VSCHD": str, "VCMOD": str, "RCOMP": str, "DELTI": str, "METER": str, "DCVMIN": str, "CCCITMX": str, "CCCACC": str}
DTYPE_TWOTERMINALDCL2KEYS = {"IPR": str, "NBR": str, "ANMXR": str, "ANMNR": str, "RCR": str, "XCR": str, "EBASR": str, "TRR": str, "TAPR": str, "TMXR": str, "TMNR": str, "STPR": str, "ICR": str, "IFR": str, "ITR": str, "IDR": str, "XCAPR": str, "NDR": str}
DTYPE_TWOTERMINALDCL3KEYS={"IPI": str, "NBI": str, "ANMXI": str, "ANMNI": str, "RCI": str, "XCI": str, "EBASI": str, "TRI": str, "TAPI": str, "TMXI": str, "TMNI": str, "STPI": str, "ICI": str, "IFI": str, "ITI": str, "IDI": str, "XCAPI": str, "NDI": str}
DTYPE_VSCDCLINEL1KEYS = {"NAME": str, "MDC": str, "RDC": str, "O1": str, "F1": str, "O2": str, "F2": str, "O3": str, "F3": str, "O4": str, "F4": str}
DTYPE_VSCDCLINEL2KEYS = {"IBUS": str, "TYPE": str, "MODE": str, "DCSET": str, "ACSET": str, "ALOSS": str, "BLOSS": str, "MINLOSS": str, "SMAX": str, "IMAX": str, "PWF": str, "MAXQ": str, "MINQ": str, "VSREG": str, "RMPCT": str, "NREG": str}
DTYPE_IMPEDANCECORRECTIONL1KEYS = {"I": str, "T1": str, "Re(F1)": str, "Im(F1)": str, "T2": str, "Re(F2)": str, "Im(F2)": str, "T3": str, "Re(F3)": str, "Im(F3)": str, "T4": str, "Re(F4)": str, "Im(F4)": str, "T5": str, "Re(F5)": str, "Im(F5)": str, "T6": str, "Re(F6)": str, "Im(F6)": str}
DTYPE_IMPEDANCECORRECTIONL2KEYS = {"T7": str, "Re(F7)": str, "Im(F7)": str, "T8": str, "Re(F8)": str, "Im(F8)": str, "T9": str, "Re(F9)": str, "Im(F9)": str, "T10": str, "Re(F10)": str, "Im(F10)": str, "T11": str, "Re(F11)": str, "Im(F11)": str, "T12": str, "Re(F12)": str, "Im(F12)": str}
DTYPE_MULTITERMINALDCL1KEYS = {"NAME": str,"NCONV": str,"NDCBS": str,"NDCLN": str,"MDC": str,"VCONV": str,"VCMOD": str,"VCONVN": str}
DTYPE_MULTITERMINALDCL2KEYS = {"IB": str, "N": str, "ANGMX": str, "ANGMN": str, "RC": str, "XC": str, "EBAS": str, "TR": str, "TAP": str, "TPMX": str, "TPMN": str, "TSTP": str, "SETVL": str, "DCPF": str, "MARG": str, "CNVCOD": str}
DTYPE_MULTITERMINALDCL3KEYS = {"IDC": str,"IB": str,"AREA": str,"ZONE": str,"DCNAME": str,"IDC2": str,"RGRND": str,"OWNER": str}
DTYPE_MULTITERMINALDCL4KEYS = {"IDC": str,"JDC": str,"DCCKT": str,"MET": str,"RDC": str,"LDC": str}
DTYPE_MULTISECTIONLINEKEYS = {"I": str, "J": str, "'ID'": str, "MET": str, "DUM1": str, "DUM2": str, "DUM3": str, "DUM4": str, "DUM5": str, "DUM6": str, "DUM7": str, "DUM8": str, "DUM9": str}
DTYPE_ZONEKEYS = {"I": str,"ZONAME": str}
DTYPE_INTERAREATRANSFERKEYS = {"ARFROM": str, "ARTO": str, "TRID": str, "PTRAN": str}
DTYPE_OWNERKEYS = {"I": str, "OWNAME": str}
DTYPE_FACTSKEYS = {"NAME": str,"I": str,"J": str,"MODE": str,"PDES": str,"QDES": str,"VSET": str,"SHMX": str,"TRMX": str,"VTMN": str,"VTMX": str,"VSMX": str,"IMX": str,"LINX": str,"RMPCT": str,"OWNER": str,"SET1": str,"SET2": str,"VSREF": str,"FCREG": str,"'MNAME'": str,"NREG": str}
DTYPE_SWITCHEDSHUNTKEYS = {"I": str, "MODSW": str, "ADJM": str, "ST": str, "VSWHI": str, "VSWLO": str, "SWREG": str, "RMPCT": str, "RMIDNT": str, "BINIT": str, "N1": str, "B1": str, "N2": str, "B2": str, "N3": str, "B3": str, "N4": str, "B4": str, "N5": str, "B5": str, "N6": str, "B6": str, "N7": str, "B7": str, "N8": str, "B8": str, "NREG": str}
DTYPE_GNEKEYS = {} # Not supported yet
DTYPE_INDUCTIONMACHINEKEYS={"I": str, "'ID'": str, "ST": str, "SC": str, "DC": str, "AREA": str, "ZONE": str, "OWNER": str, "TC": str, "BC": str, "MBASE": str, "RATEKV": str, "PC": str, "PSET": str, "H": str, "A": str, "B": str, "D": str, "E": str, "RA": str, "XA": str, "XM": str, "R1": str, "X1": str, "R2": str, "X2": str, "X3": str, "E1": str, "SE1": str, "E2": str, "SE2": str, "IA1": str, "IA2": str, "XAMULT": str}
DTYPE_SUBSTATIONKEYS = {}

RAW_DATA = {
    "HEADER": HEADERKEYS,
    "BUS": BUSKEYS,
    "LOAD": LOADKEYS,
    "FIXED SHUNT": FIXEDSHUNTKEYS,
    "GENERATOR": GENERATORKEYS,
    "BRANCH": BRANCHKEYS,
    "SYSTEM SWITCHING DEVICE": SYSTEMSWITCHINGDEVICEKEYS,
    "TRANSFORMER": [TRANSFORMERP1KEYS, TRANSFORMERP2KEYS, TRANSFORMERL1KEYS, TRANSFORMERL2KEYS, TRANSFORMERL3KEYS],
    "AREA": AREAKEYS,
    "TWO-TERMINAL DC": [TWOTERMINALDCL1KEYS, TWOTERMINALDCL2KEYS, TWOTERMINALDCL3KEYS],
    "VSC DC LINE": [VSCDCLINEL1KEYS, VSCDCLINEL2KEYS],
    "IMPEDANCE CORRECTION": [IMPEDANCECORRECTIONL1KEYS, IMPEDANCECORRECTIONL2KEYS],
    "MULTI-TERMINAL DC": [MULTITERMINALDCL1KEYS, MULTITERMINALDCL2KEYS, MULTITERMINALDCL3KEYS, MULTITERMINALDCL4KEYS],
    "MULTI-SECTION LINE": MULTISECTIONLINEKEYS,
    "ZONE": ZONEKEYS,
    "INTER-AREA TRANSFER": INTERAREATRANSFERKEYS,
    "OWNER": OWNERKEYS,
    "FACTS": FACTSKEYS,
    "SWITCHED SHUNT": SWITCHEDSHUNTKEYS,
    "GNE": GNEKEYS,
    "INDUCTION MACHINE": INDUCTIONMACHINEKEYS,
    "SUBSTATION": SUBSTATIONKEYS
    }

DTYPE_RAW_DATA = {
    "HEADER": DTYPE_HEADERKEYS,
    "BUS": DTYPE_BUSKEYS,
    "LOAD": DTYPE_LOADKEYS,
    "FIXED SHUNT": DTYPE_FIXEDSHUNTKEYS,
    "GENERATOR": DTYPE_GENERATORKEYS,
    "BRANCH": DTYPE_BRANCHKEYS,
    "SYSTEM SWITCHING DEVICE": DTYPE_SYSTEMSWITCHINGDEVICEKEYS,
    "TRANSFORMER": [DTYPE_TRANSFORMERP1KEYS, DTYPE_TRANSFORMERP2KEYS, DTYPE_TRANSFORMERL1KEYS, DTYPE_TRANSFORMERL2KEYS, DTYPE_TRANSFORMERL3KEYS],
    "AREA": DTYPE_AREAKEYS,
    "TWO-TERMINAL DC": [DTYPE_TWOTERMINALDCL1KEYS, DTYPE_TWOTERMINALDCL2KEYS, DTYPE_TWOTERMINALDCL3KEYS],
    "VSC DC LINE": [DTYPE_VSCDCLINEL1KEYS, DTYPE_VSCDCLINEL2KEYS],
    "IMPEDANCE CORRECTION": [DTYPE_IMPEDANCECORRECTIONL1KEYS, DTYPE_IMPEDANCECORRECTIONL2KEYS],
    "MULTI-TERMINAL DC": [DTYPE_MULTITERMINALDCL1KEYS, DTYPE_MULTITERMINALDCL2KEYS, DTYPE_MULTITERMINALDCL3KEYS, DTYPE_MULTITERMINALDCL4KEYS],
    "MULTI-SECTION LINE": DTYPE_MULTISECTIONLINEKEYS,
    "ZONE": DTYPE_ZONEKEYS,
    "INTER-AREA TRANSFER": DTYPE_INTERAREATRANSFERKEYS,
    "OWNER": DTYPE_OWNERKEYS,
    "FACTS": DTYPE_FACTSKEYS,
    "SWITCHED SHUNT": DTYPE_SWITCHEDSHUNTKEYS,
    "GNE": DTYPE_GNEKEYS,
    "INDUCTION MACHINE": DTYPE_INDUCTIONMACHINEKEYS,
    "SUBSTATION": DTYPE_SUBSTATIONKEYS
    }
    
MULTILINECOMPONENTS = ["TRANSFORMER", "TWO-TERMINAL DC", "VSC DC LINE", "IMPEDANCE CORRECTION", "MULTI-TERMINAL DC"]

SEQGENERATORKEYS = ["I", "ID", "ZRPOS", "ZXPPDV", "ZXPDV", "ZXSDV", "ZRNEG", "ZXNEGDV", "ZR0", "ZX0DV", "CZG", "ZRG", "ZXG", "REFDEG"]
SEQLOADKEYS = ["I", "ID", "PNEG", "QNEG", "GRDFLG", "PZERO", "QZERO"]
ZEROSEQNONTRANSFORMERBRANCHKEYS = ["I", "J", "ICKT", "RLINZ", "XLINZ", "BCHZ", "GI", "BI", "GJ", "BJ", "IPR", "SCTYP"]
ZEROSEQMUTUALDATA = ["I", "J", "ICKT1", "K", "L", "'ICKT2'", "RM", "XM", "BIJ1", "BIJ2", "BKL1", "BKL2"]
ZEROSEQ2WTRANSFORMERKEYS = ["I", "J", "K", "ICKT", "CZ0", "CZG", "CC", "RG1", "XG1", "R01", "X01", "RG2", "XG2", "R02", "X02", "RNUTRL", "XNUTRL"]
ZEROSEQ3WTRANSFORMERKEYS = ["I", "J", "K", "ICKT", "CZ0", "CZG", "CC", "RG1", "XG1", "R01", "X01", "RG2", "XG2", "R02", "X02", "RG3", "XG3", "R03", "X03", "RNUTRL", "XNUTRL"]
ZEROSEQSWITCHEDSHUNTKEYS = ["I", "BZ1", "BZ2", "BZ3", "BZ4", "BZ5", "BZ6", "BZ7", "BZ8"]
ZEROSEQFIXEDSHUNTKEYS = ["I", "ID", "GSZERO", "BSZERO"]
SEQINDUCTIONMACHINEKEYS = ["I", "ID", "CZG", "GRDFLG", "ILR2IR", "RTOX", "ZR0", "ZX0", "ZRG", "ZXG", "ILR2IR_TRN", "RTOX_TRN", "ILR2IR_NEG", "RTOX_NEG1"]
NONCONVENTIONALSOURCEFAULTCONTRIBUTIONKEYS = ["I", "ID", "T1", "C1P", "C1Q", "T2", "C2P", "C2Q", "T3", "C3P", "C3Q", "T4", "C4P", "C4Q", "T5", "C5P", "C5Q", "T6", "C6P", "C6Q"]

DTYPE_SEQGENERATORKEYS = {"I": int, "ID": str, "ZRPOS": float, "ZXPPDV": float, "ZXPDV": float, "ZXSDV": float, "ZRNEG": float, "ZXNEGDV": float, "ZR0": float, "ZX0DV": float, "CZG": float, "ZRG": float, "ZXG": float, "REFDEG": float}
DTYPE_SEQLOADKEYS = {"I": str, "ID": str, "PNEG": str, "QNEG": str, "GRDFLG": str, "PZERO": str, "QZERO": str}
DTYPE_ZEROSEQNONTRANSFORMERBRANCHKEYS = {"I": str, "J": str, "ICKT": str, "RLINZ": str, "XLINZ": str, "BCHZ": str, "GI": str, "BI": str, "GJ": str, "BJ": str, "IPR": str, "SCTYP": str}
DTYPE_ZEROSEQMUTUALDATA = {"I": str, "J": str, "ICKT1": str, "K": str, "L": str, "'ICKT2'": str, "RM": str, "XM": str, "BIJ1": str, "BIJ2": str, "BKL1": str, "BKL2": str}
DTYPE_ZEROSEQ2WTRANSFORMERKEYS = {"I": int, "J": int, "K": int, "ICKT": str, "CZ0": int, "CZG": int, "CC": int, "RG1": float, "XG1": float, "R01": float, "X01": float, "RG2": float, "XG2": float, "R02": float, "X02": float, "RNUTRL": float, "XNUTRL": float}
DTYPE_ZEROSEQ3WTRANSFORMERKEYS = {"I": int, "J": int, "K": int, "ICKT": str, "CZ0": int, "CZG": int, "CC": int, "RG1": float, "XG1": float, "R01": float, "X01": float, "RG2": float, "XG2": float, "R02": float, "X02": float, "RG3": float, "XG3": float, "R03": float, "X03": float, "RNUTRL": float, "XNUTRL": float}
DTYPE_ZEROSEQSWITCHEDSHUNTKEYS = {"I": str, "BZ1": str, "BZ2": str, "BZ3": str, "BZ4": str, "BZ5": str, "BZ6": str, "BZ7": str, "BZ8": str}
DTYPE_ZEROSEQFIXEDSHUNTKEYS = {"I": str, "ID": str, "GSZERO": str, "BSZERO": str}
DTYPE_SEQINDUCTIONMACHINEKEYS = {"I": str, "ID": str, "CZG": str, "GRDFLG": str, "ILR2IR": str, "RTOX": str, "ZR0": str, "ZX0": str, "ZRG": str, "ZXG": str, "ILR2IR_TRN": str, "RTOX_TRN": str, "ILR2IR_NEG": str, "RTOX_NEG1": str}
DTYPE_NONCONVENTIONALSOURCEFAULTCONTRIBUTIONKEYS = {"I": str, "ID": str, "T1": str, "C1P": str, "C1Q": str, "T2": str, "C2P": str, "C2Q": str, "T3": str, "C3P": str, "C3Q": str, "T4": str, "C4P": str, "C4Q": str, "T5": str, "C5P": str, "C5Q": str, "T6": str, "C6P": str, "C6Q": str}

SEQ_DATA = {
    "GENERATOR": SEQGENERATORKEYS,
    "LOAD": SEQLOADKEYS,
    "ZERO SEQ. MUTUAL": ZEROSEQMUTUALDATA,
    "ZERO SEQ. NON-TRANSFORMER BRANCH": ZEROSEQNONTRANSFORMERBRANCHKEYS,
    "ZERO SEQ. TRANSFORMER": [ZEROSEQ2WTRANSFORMERKEYS, ZEROSEQ3WTRANSFORMERKEYS],
    "ZERO SEQ. SWITCHED SHUNT": ZEROSEQSWITCHEDSHUNTKEYS,
    "ZERO SEQ. FIXED SHUNT": ZEROSEQFIXEDSHUNTKEYS,
    "INDUCTION MACHINE": SEQINDUCTIONMACHINEKEYS,
    "NON CONVENTIONAL SOURCE FAULT CONTRIBUTION": NONCONVENTIONALSOURCEFAULTCONTRIBUTIONKEYS,
}

DTYPE_SEQ_DATA = {
    "GENERATOR": DTYPE_SEQGENERATORKEYS,
    "LOAD": DTYPE_SEQLOADKEYS,
    "ZERO SEQ. MUTUAL": DTYPE_ZEROSEQMUTUALDATA,
    "ZERO SEQ. NON-TRANSFORMER BRANCH": DTYPE_ZEROSEQNONTRANSFORMERBRANCHKEYS,
    "ZERO SEQ. TRANSFORMER": [DTYPE_ZEROSEQ2WTRANSFORMERKEYS, DTYPE_ZEROSEQ3WTRANSFORMERKEYS],
    "ZERO SEQ. SWITCHED SHUNT": DTYPE_ZEROSEQSWITCHEDSHUNTKEYS,
    "ZERO SEQ. FIXED SHUNT": DTYPE_ZEROSEQFIXEDSHUNTKEYS,
    "INDUCTION MACHINE": DTYPE_SEQINDUCTIONMACHINEKEYS,
    "NON CONVENTIONAL SOURCE FAULT CONTRIBUTION": DTYPE_NONCONVENTIONALSOURCEFAULTCONTRIBUTIONKEYS,
}
