site1_g_carbon_m2_day = 5
site2_g_carbon_m2_day = 2.3
site1_area_m2 = 200
site2_area_m2 = 450
site1_npp_day = site1_g_carbon_m2_day * site1_area_m2 
site2_npp_day = site2_g_carbon_m2_day * site2_area_m2
site1_npp_year = site1_g_carbon_m2_day * 365 * site1_area_m2 
site2_npp_year = site2_g_carbon_m2_day * 365 * site2_area_m2


sites_total_day = site1_npp_day + site2_npp_day
sites_difference = abs(site1_npp_day - site2_npp_day)
sites_total_year = site1_npp_year + site2_npp_year

print(sites_total_day)
print(sites_difference)
print(sites_total_year)
