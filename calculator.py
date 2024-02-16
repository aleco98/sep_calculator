us_federal_tax_brackets_2024={
        'bracket_1':.1,
        'bracket_2':.12,
        'bracket_3':.22,
        'bracket_4':.24,
        'bracket_5':.32,
        'bracket_6':.35,
        'bracket_7':.37
    }

us_federal_tax_brackets_2023={
        'bracket_1':.1,
        'bracket_2':.12,
        'bracket_3':.22,
        'bracket_4':.24,
        'bracket_5':.32,
        'bracket_6':.35,
        'bracket_7':.37
    }
# change


def tax_calculator_for_married_filing_jointly(taxable_income, tax_year):
    if tax_year==2024:
        if taxable_income<=23200:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=94300: 
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-23200))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        elif taxable_income<=201050:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-94300))+(us_federal_tax_brackets_2024['bracket_2']*(71100))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        elif taxable_income<=383900:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-201050))+(us_federal_tax_brackets_2024['bracket_3']*(106750))+(us_federal_tax_brackets_2024['bracket_2']*(71100))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        elif taxable_income<=487450:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-383900))+(us_federal_tax_brackets_2024['bracket_4']*(182850))+(us_federal_tax_brackets_2024['bracket_3']*(106750))+(us_federal_tax_brackets_2024['bracket_2']*(71100))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        elif taxable_income<=731200:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-487450))+(us_federal_tax_brackets_2024['bracket_5']*(103550))+(us_federal_tax_brackets_2024['bracket_4']*(182850))+(us_federal_tax_brackets_2024['bracket_3']*(106750))+(us_federal_tax_brackets_2024['bracket_2']*(71100))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        elif taxable_income>731200:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-731200))+(us_federal_tax_brackets_2024['bracket_6']*(243750))+(us_federal_tax_brackets_2024['bracket_5']*(103550))+(us_federal_tax_brackets_2024['bracket_4']*(182850))+(us_federal_tax_brackets_2024['bracket_3']*(106750))+(us_federal_tax_brackets_2024['bracket_2']*(71100))+(us_federal_tax_brackets_2024['bracket_1']*23200)
        return federal_tax_liability
    elif tax_year==2023:
        if taxable_income<=22000:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=89450:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-22000))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        elif taxable_income<=190750:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-89450))+(us_federal_tax_brackets_2024['bracket_2']*(67450))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        elif taxable_income<=364200:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-190750))+(us_federal_tax_brackets_2024['bracket_3']*(101300))+(us_federal_tax_brackets_2024['bracket_2']*(67450))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        elif taxable_income<=462500:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-364200))+(us_federal_tax_brackets_2024['bracket_4']*(173450))+(us_federal_tax_brackets_2024['bracket_3']*(101300))+(us_federal_tax_brackets_2024['bracket_2']*(67450))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        elif taxable_income<=693750:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-462500))+(us_federal_tax_brackets_2024['bracket_5']*(98300))+(us_federal_tax_brackets_2024['bracket_4']*(173450))+(us_federal_tax_brackets_2024['bracket_3']*(101300))+(us_federal_tax_brackets_2024['bracket_2']*(67450))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        elif taxable_income>693750:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-693750))+(us_federal_tax_brackets_2024['bracket_6']*(231250))+(us_federal_tax_brackets_2024['bracket_5']*(98300))+(us_federal_tax_brackets_2024['bracket_4']*(173450))+(us_federal_tax_brackets_2024['bracket_3']*(101300))+(us_federal_tax_brackets_2024['bracket_2']*(67450))+(us_federal_tax_brackets_2024['bracket_1']*22000)
        return federal_tax_liability

def tax_calculator_for_single_filer(taxable_income, tax_year):
    if tax_year==2024:
        if taxable_income<=11600:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=47150:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-11600))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        elif taxable_income<=100525:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-47150))+(us_federal_tax_brackets_2024['bracket_2']*(35550))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        elif taxable_income<=191950:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-100525))+(us_federal_tax_brackets_2024['bracket_3']*(53375))+(us_federal_tax_brackets_2024['bracket_2']*(35550))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        elif taxable_income<=243725:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-191950))+(us_federal_tax_brackets_2024['bracket_4']*(91425))+(us_federal_tax_brackets_2024['bracket_3']*(53375))+(us_federal_tax_brackets_2024['bracket_2']*(35550))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        elif taxable_income<=609350:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-243725))+(us_federal_tax_brackets_2024['bracket_5']*(51775))+(us_federal_tax_brackets_2024['bracket_4']*(91425))+(us_federal_tax_brackets_2024['bracket_3']*(53375))+(us_federal_tax_brackets_2024['bracket_2']*(35550))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        elif taxable_income>609350:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-609350))+(us_federal_tax_brackets_2024['bracket_6']*(365625))+(us_federal_tax_brackets_2024['bracket_5']*(51775))+(us_federal_tax_brackets_2024['bracket_4']*(91425))+(us_federal_tax_brackets_2024['bracket_3']*(53375))+(us_federal_tax_brackets_2024['bracket_2']*(35550))+(us_federal_tax_brackets_2024['bracket_1']*11600)
        return federal_tax_liability
    elif tax_year==2023:
        if taxable_income<=11000:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=44725:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        elif taxable_income<=95375:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-44725))+(us_federal_tax_brackets_2024['bracket_2']*(33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        elif taxable_income<=182100:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-95375))+(us_federal_tax_brackets_2024['bracket_3']*(50650))+(us_federal_tax_brackets_2024['bracket_2']*(33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        elif taxable_income<=231250:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-182100))+(us_federal_tax_brackets_2024['bracket_4']*(86725))+(us_federal_tax_brackets_2024['bracket_3']*(50650))+(us_federal_tax_brackets_2024['bracket_2']*(33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        elif taxable_income<=578125:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-231250))+(us_federal_tax_brackets_2024['bracket_5']*(49150))+(us_federal_tax_brackets_2024['bracket_4']*(86725))+(us_federal_tax_brackets_2024['bracket_3']*(50650))+(us_federal_tax_brackets_2024['bracket_2']*(33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        elif taxable_income>578125:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-578125))+(us_federal_tax_brackets_2024['bracket_6']*(346875))+(us_federal_tax_brackets_2024['bracket_5']*(49150))+(us_federal_tax_brackets_2024['bracket_4']*(86725))+(us_federal_tax_brackets_2024['bracket_3']*(50650))+(us_federal_tax_brackets_2024['bracket_2']*(33725))+(us_federal_tax_brackets_2024['bracket_1']*11000)
        return federal_tax_liability

def tax_calculator_for_head_of_household(taxable_income, tax_year):
    if tax_year==2024:
        if taxable_income<=16550:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=63100:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-16550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        elif taxable_income<=100500:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-63100))+(us_federal_tax_brackets_2024['bracket_2']*(46550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        elif taxable_income<=191950:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-100500))+(us_federal_tax_brackets_2024['bracket_3']*(37400))+(us_federal_tax_brackets_2024['bracket_2']*(46550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        elif taxable_income<=243700:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-191950))+(us_federal_tax_brackets_2024['bracket_4']*(91450))+(us_federal_tax_brackets_2024['bracket_3']*(37400))+(us_federal_tax_brackets_2024['bracket_2']*(46550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        elif taxable_income<=609350:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-243700))+(us_federal_tax_brackets_2024['bracket_5']*(51750))+(us_federal_tax_brackets_2024['bracket_4']*(91450))+(us_federal_tax_brackets_2024['bracket_3']*(37400))+(us_federal_tax_brackets_2024['bracket_2']*(46550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        elif taxable_income>609350:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-609350))+(us_federal_tax_brackets_2024['bracket_6']*(365650))+(us_federal_tax_brackets_2024['bracket_5']*(51750))+(us_federal_tax_brackets_2024['bracket_4']*(91450))+(us_federal_tax_brackets_2024['bracket_3']*(37400))+(us_federal_tax_brackets_2024['bracket_2']*(46550))+(us_federal_tax_brackets_2024['bracket_1']*16550)
        return federal_tax_liability
    elif tax_year==2023: # Updated
        if taxable_income<=15700:
            federal_tax_liability=us_federal_tax_brackets_2024['bracket_1']*taxable_income
        elif taxable_income<=59850:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_2']*(taxable_income-15700))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        elif taxable_income<=95350:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_3']*(taxable_income-59850))+(us_federal_tax_brackets_2024['bracket_2']*(44150))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        elif taxable_income<=182100:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_4']*(taxable_income-95350))+(us_federal_tax_brackets_2024['bracket_3']*(35500))+(us_federal_tax_brackets_2024['bracket_2']*(44150))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        elif taxable_income<=231250:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_5']*(taxable_income-182100))+(us_federal_tax_brackets_2024['bracket_4']*(86750))+(us_federal_tax_brackets_2024['bracket_3']*(35500))+(us_federal_tax_brackets_2024['bracket_2']*(44150))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        elif taxable_income<=578100:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_6']*(taxable_income-231250))+(us_federal_tax_brackets_2024['bracket_5']*(49150))+(us_federal_tax_brackets_2024['bracket_4']*(86750))+(us_federal_tax_brackets_2024['bracket_3']*(35500))+(us_federal_tax_brackets_2024['bracket_2']*(44150))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        elif taxable_income>578100:
            federal_tax_liability=(us_federal_tax_brackets_2024['bracket_7']*(taxable_income-578100))+(us_federal_tax_brackets_2024['bracket_6']*(346850))+(us_federal_tax_brackets_2024['bracket_5']*(49150))+(us_federal_tax_brackets_2024['bracket_4']*(86750))+(us_federal_tax_brackets_2024['bracket_3']*(35500))+(us_federal_tax_brackets_2024['bracket_2']*(44150))+(us_federal_tax_brackets_2024['bracket_1']*15700)
        return federal_tax_liability


def sep_ira_contribution_limit_calculator(income, tax_year, contribution_rate, filing_status):
    # Limit calculator for self employed individuals
    if tax_year==2024:
        ss_income_cap=168600 # social security income cap
        ss_tax_rate=.124 # social security tax rate, all borne by self employed person in this case
        medicare_tax_rate=.029 # medicare tax rate
        sep_contribution_cap=69000
        self_employment_tax_adjuster=.9235 # Employer portion of tax is 7.65%, so that can be subtracted from self-employed taxpayers' rate.
        medicare_tax=income*self_employment_tax_adjuster*medicare_tax_rate
        if income<ss_income_cap:
            ss_tax=income*ss_tax_rate*self_employment_tax_adjuster
            self_employment_tax=ss_tax+medicare_tax
        elif income>=ss_income_cap:
            ss_tax=ss_income_cap*ss_tax_rate*self_employment_tax_adjuster
            self_employment_tax=ss_tax+medicare_tax
        deductible_part_of_self_employment_tax=self_employment_tax*.5
        net_earnings=income-deductible_part_of_self_employment_tax
        special_contribution_rate=contribution_rate/(contribution_rate+1)
        if net_earnings*special_contribution_rate>=sep_contribution_cap:
            sep_contribution=sep_contribution_cap
        else:
            sep_contribution=net_earnings*special_contribution_rate
        # Now calculate savings
        if filing_status == 1: # 1 for indivudal
            tax_before_sep=tax_calculator_for_single_filer(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_single_filer(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
        elif filing_status ==2: # for married filing jointly
            tax_before_sep=tax_calculator_for_married_filing_jointly(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_married_filing_jointly(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
        elif filing_status ==3: # for head of household
            tax_before_sep=tax_calculator_for_head_of_household(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_head_of_household(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
    elif tax_year==2023:
        ss_income_cap=160200 # social security income cap
        ss_tax_rate=.124 # social security tax rate, all borne by self employed person in this case
        medicare_tax_rate=.029 # medicare tax rate
        sep_contribution_cap=66000
        self_employment_tax_adjuster=.9235 # Employer portion of tax is 7.65%, so that can be subtracted from self-employed taxpayers' rate.
        medicare_tax=income*self_employment_tax_adjuster*medicare_tax_rate
        if income<ss_income_cap:
            ss_tax=income*ss_tax_rate*self_employment_tax_adjuster
            self_employment_tax=ss_tax+medicare_tax
        elif income>=ss_income_cap:
            ss_tax=ss_income_cap*ss_tax_rate*self_employment_tax_adjuster
            self_employment_tax=ss_tax+medicare_tax
        deductible_part_of_self_employment_tax=self_employment_tax*.5
        net_earnings=income-deductible_part_of_self_employment_tax
        special_contribution_rate=contribution_rate/(contribution_rate+1)
        if net_earnings*special_contribution_rate>=sep_contribution_cap:
            sep_contribution=sep_contribution_cap
        else:
            sep_contribution=net_earnings*special_contribution_rate
        if filing_status == 1: # 1 for indivudal
            tax_before_sep=tax_calculator_for_single_filer(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_single_filer(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
        elif filing_status ==2: # for married filing jointly
            tax_before_sep=tax_calculator_for_married_filing_jointly(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_married_filing_jointly(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
        elif filing_status ==3: # for head of household
            tax_before_sep=tax_calculator_for_head_of_household(net_earnings, tax_year)
            tax_after_sep=tax_calculator_for_head_of_household(net_earnings-sep_contribution, tax_year)
            tax_savings=tax_before_sep-tax_after_sep
            return tax_before_sep, tax_after_sep, tax_savings, sep_contribution
    else:
        pass
