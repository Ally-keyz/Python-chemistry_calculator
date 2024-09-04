import pyttsx3
engine = pyttsx3.init()

equations={
    # Combustion Reactions
    "H2O2":"2 H2 + O2 -> 2 H2O",
    "CO2":"C + O2 -> CO2",
    "MGO2":"2 Mg + O2 -> 2 MgO",
    "PO2":"4 P + 5 O2 -> 2 P2O5",
    "CH4O2":"CH4 + 2 O2 -> CO2 + 2 H2O",
    "H2SO2":"2 H2S + 3 O2 -> 2 SO2 + 2 H2O",
            
    # Acid-Base Reactions
    "HCLNAOH":"HCl + NaOH -> NaCl + H2O",
    "H2SO4NAOH":"H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O",
    "NH3H2O":"NH3 + H2O -> NH4OH",
    "H2SO4CA(OH)2":"H2SO4 + Ca(OH)2 -> CaSO4 + 2 H2O",
    "H3PO4NAOH":"H3PO4 + 3 NaOH -> Na3PO4 + 3 H2O",
            
    # Single Displacement Reactions
    "NACL":"2 Na + Cl2 -> 2 NaCl",
    "ZNHCL":"Zn + 2 HCl -> ZnCl2 + H2",
    "CAH2O":"Ca + 2 H2O -> Ca(OH)2 + H2",
    "ALCUCL2":"2 Al + 3 CuCl2 -> 2 AlCl3 + 3 Cu",
    "KH2O":"2 K + 2 H2O -> 2 KOH + H2",
            
    # Double Displacement Reactions
    "AGNO3NACL":"AgNO3 + NaCl -> AgCl + NaNO3",
    "BACLH2SO4":"BaCl2 + H2SO4 -> BaSO4 + 2 HCl",
    "CACO3HCL":"CaCO3 + 2 HCl -> CaCl2 + CO2 + H2O",
    "NA2CO3HCL":"Na2CO3 + HCl -> NaCl + H2O + CO2",
    "NA2SO4BACL2":"Na2SO4 + BaCl2 -> BaSO4 + 2 NaCl",
            
    # Synthesis Reactions
    "N2H2":"N2 + 3 H2 -> 2 NH3",
    "KCL2":"2 K + Cl2 -> 2 KCl",
    "CAOCO2":"CaO + CO2 -> CaCO3",
    "ALCL2":"2 Al + 3 Cl2 -> 2 AlCl3",
    "SIO2HF":"SiO2 + 4 HF -> SiF4 + 2 H2O",
    "NAO2":"2 Na + O2 -> Na2O2",
    "H2N2":"3 H2 + N2 -> 2 NH3",
    "PO2":"P4 + 5 O2 -> 2 P2O5",
    "CACL2":"Ca + Cl2 -> CaCl2",
    "KBR2":"2 K + Br2 -> 2 KBr",
            
    # Decomposition Reactions
    "H2OO2":"2 H2O -> 2 H2 + O2",
    "CACO3O2":"CaCO3 -> CaO + CO2",
    "NACLO2":"2 NaCl -> 2 Na + Cl2",
    "KCLO3O2":"2 KClO3 -> 2 KCl + 3 O2",
    "HGOO2":"2 HgO -> 2 Hg + O2",
    "H2CO3O2":"H2CO3 -> CO2 + H2O",
    "NH4CLO2":"2 NH4Cl -> 2 NH3 + Cl2",
    "AL2(CO3)3O2":"Al2(CO3)3 -> Al2O3 + 3 CO2",
    "AG2OO2":"2 Ag2O -> 4 Ag + O2",
            
    # Redox Reactions
    "H2O20":"2 H2O2 -> 2 H2O + O2",
    "ZNCUSO4":"Zn + CuSO4 -> ZnSO4 + Cu",
    "FE2O3CO":"Fe2O3 + 3 CO -> 2 Fe + 3 CO2",
    "ALFE2O3":"2 Al + Fe2O3 -> 2 Fe + Al2O3",
    "CL2KI":"Cl2 + 2 KI -> 2 KCl + I2",
            
    # Precipitation Reactions
    "NA2SO4BACL2":"Na2SO4 + BaCl2 -> BaSO4 + 2 NaCl",
    "CACL2NA2CO3":"CaCl2 + Na2CO3 -> CaCO3 + 2 NaCl",
    "AGNO3KCL":"AgNO3 + KCl -> AgCl + KNO3",
    "PB(NO3)2KI":"Pb(NO3)2 + 2 KI -> PbI2 + 2 KNO3",
    "CA(OH)2CO2":"Ca(OH)2 + CO2 -> CaCO3 + H2O",
            
    # Additional Reactions
    "LIH2O":"2 Li + 2 H2O -> 2 LiOH + H2",
    "FEO":"4 Fe + 3 O2 -> 2 Fe2O3",
    "ALH2SO4":"2 Al + 3 H2SO4 -> Al2(SO4)3 + 3 H2",
    "SIO2HF":"SiO2 + 4 HF -> SiF4 + 2 H2O",
    "KH":"2 K + H2 -> 2 KH",
    "NAO":"2 Na + O2 -> Na2O2",
    "MGHCL":"Mg + 2 HCl -> MgCl2 + H2",
    "NAH2O":"2 Na + 2 H2O -> 2 NaOH + H2",
    "KH2O":"2 K + 2 H2O -> 2 KOH + H2",
    "CAH2O":"Ca + 2 H2O -> Ca(OH)2 + H2",
    "ZNHCL":"Zn + 2 HCl -> ZnCl2 + H2",
    "FES":"Fe + S -> FeS",
    "H2N2":"3 H2 + N2 -> 2 NH3",
    "NAO2":"4 Na + O2 -> 2 Na2O",
    "MGN2":"3 Mg + N2 -> Mg3N2",
    "ALI2":"2 Al + 3 I2 -> 2 AlI3",
    "ALBR2":"2 Al + 3 Br2 -> 2 AlBr3",
    "ALS":"2 Al + 3 S -> Al2S3",
    "MGALCL3":"3 Mg + 2 AlCl3 -> 3 MgCl2 + 2 Al",
    "CUHNO3":"3 Cu + 8 HNO3 -> 3 Cu(NO3)2 + 2 NO + 4 H2O",
    "ZNCU(NO3)2":"Zn + Cu(NO3)2 -> Zn(NO3)2 + Cu",
    "NAALCL3":"3 Na + AlCl3 -> 3 NaCl + Al",
    "CAH2O":"Ca + 2 H2O -> Ca(OH)2 + H2",
    "NAH2O":"2 Na + 2 H2O -> 2 NaOH + H2",
    "CL2NAI":"Cl2 + 2 NaI -> 2 NaCl + I2",
    "BRNAI":"Br2 + 2 NaI -> 2 NaBr + I2",
    "FECL2":"2 Fe + 3 Cl2 -> 2 FeCl3",
    "ALCL2":"2 Al + 3 Cl2 -> 2 AlCl3",
    "FEI2":"2 Fe + 3 I2 -> 2 FeI3",
    "ZNHCL":"Zn + 2 HCl -> ZnCl2 + H2",
    "KH2O":"2 K + 2 H2O -> 2 KOH + H2",
    "BAH2O":"Ba + 2 H2O -> Ba(OH)2 + H2",
    "H2O2":"2 H2 + O2 -> 2 H2O",
    "MGH2O":"Mg + 2 H2O -> Mg(OH)2 + H2",
    "NAH2O":"Na + H2O -> NaOH + H2",
    "H2N2":"3 H2 + N2 -> 2 NH3",
    "HCLMG":"2 HCl + Mg -> MgCl2 + H2",
    "CL2NABR":"Cl2 + 2 NaBr -> 2 NaCl + Br2",
    "H2SO4NAOH":"H2SO4 + 2 NaOH -> Na2SO4 + 2 H2O",
    "HNO3KOH":"HNO3 + KOH -> KNO3 + H2O",
    "NACL":"NaCl + AgNO3 -> NaNO3 + AgCl",
    "HCLNAHCO3":"HCl + NaHCO3 -> NaCl + CO2 + H2O",
    "FECL2":"2 Fe + 3 Cl2 -> 2 FeCl3",
    "CAALCL3":"3 Ca + 2 AlCl3 -> 3 CaCl2 + 2 Al",
}

    

def main():
    equa1 = get_equa1()
    equa2 = get_equa2()
    equa = combine_equation(equa1,equa2)
    equationF = formulate_equation(equa)
    print(f"The equation is: {equationF}")
    engine.say(f"The equation is {equationF}")
    engine.runAndWait()
     



def get_equa1():
    while True:
        try:
            numA = input("Enter first reactant: ").upper()
        
        except ValueError:
            print("please try again !!")
        return numA

   




def get_equa2():

    while True:
        try:
            numB= input("Enter second reactant: ").upper()
        except ValueError:
            engine.say("please try again")
            engine.runAndWait()
            engine.runAndWait()
        return numB 


def combine_equation(equa1,equa2):
    outcome = equa1 + equa2
    return outcome


def formulate_equation(equation):
    if equation in equations:
        return equations[equation]

    else:
        engine.say("Equation not surported")
        engine.runAndWait()
        return None    

main()