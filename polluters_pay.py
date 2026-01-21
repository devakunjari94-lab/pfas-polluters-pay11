import streamlit as st

st.title("Polluters-Pay Calculator")

# Inputs
site_name = st.text_input("Site Name")
pfas_conc = st.number_input("PFAS Concentration (ng/L or ng/kg)", value=1200000.0)
water_volume = st.number_input("Volume of water to clean (m³)", value=1000000.0)
soil_area = st.number_input("Soil area to clean (hectares)", value=10.0)

# Cost methods (£/m³)
methods = {
    "GAC": 0.06,
    "IX": 0.08,
    "RO": 0.15,
    "Oxyle": 0.001,
    "Wetlands": 0.01
}

st.subheader("Total cost to clean water:")

# Calculate and display cost per method
total_costs = {}
for method, cost_per_m3 in methods.items():
    total = water_volume * cost_per_m3
    total_costs[method] = total
    st.write(f"{method}: £{total:,.0f}")

# Soil cleaning (example calculation)
st.subheader("Total cost to clean soil (estimate)")
soil_cost_per_hectare = 50000  # £ per hectare
total_soil_cost = soil_area * soil_cost_per_hectare
st.write(f"Soil cleanup: £{total_soil_cost:,.0f}")

# Grand total
grand_total = sum(total_costs.values()) + total_soil_cost
st.subheader("Grand Total")
st.write(f"£{grand_total:,.0f}")
