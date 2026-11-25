# openLCA parameters and formulas

Generated from `openlca/SiToLub_parametrised_processes.zip` by `scripts/list_formulas.py`.

`amt` stands for the original ecoinvent 3.12 cut-off amount of the exchange.

## Global parameters

| Parameter | Default | Formula |
|---|---|---|
| `lifetime_ref` | 150000 |  |
| `sump_life` | 2000 |  |
| `electricity_mwf_benchmark` | 1.15 |  |
| `diesel_consumption` | 0.060648 |  |
| `lube_production` | 0.00929 |  |
| `electricity_forming` | 0.0333 |  |
| `machine_output_forming` | 12837 |  |
| `lube_mwf_benchmark` | 0.000867 |  |
| `machine_output_mwf_benchmark` | 25316.46 |  |
| `oil_fill_benchmark` | 4.18 |  |
| `lube_mwf` | 0.000867 |  |
| `fuel_factor` | 1 | `diesel_consumption / diesel_consumption_benchmark` |
| `machine_output_forming_benchmark` | 12837 |  |
| `lube_production_benchmark` | 0.00929 |  |
| `electricity_mwf` | 1.15 |  |
| `drain_interval` | 15000 |  |
| `lifetime_km` | 150000 |  |
| `lube_forming` | 0 |  |
| `diesel_consumption_benchmark` | 0.060648 |  |
| `oil_fill` | 4.18 |  |
| `drain_interval_benchmark` | 15000 |  |
| `electricity_forming_benchmark` | 0.0333 |  |
| `sump_life_benchmark` | 2000 |  |
| `machine_output_mwf` | 25316.46 |  |

## Parametrised processes (30)

### deep drawing, steel, 650 kN press, automode | deep drawing, steel, 650 kN press, automode | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_forming / electricity_forming_benchmark` |
| input | lubricating oil | `lube_forming` |
| input | metal working machine, unspecified | `amt * machine_output_forming_benchmark / machine_output_forming` |
| output | waste mineral oil | `lube_forming` |

### deep drawing, steel, 650 kN press, automode | deep drawing, steel, 650 kN press, automode | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_forming / electricity_forming_benchmark` |
| input | lubricating oil | `lube_forming` |
| input | metal working machine, unspecified | `amt * machine_output_forming_benchmark / machine_output_forming` |
| output | waste mineral oil | `lube_forming` |

### deep drawing, steel, 650 kN press, single stroke | deep drawing, steel, 650 kN press, single stroke | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_forming / electricity_forming_benchmark` |
| input | lubricating oil | `lube_forming` |
| input | metal working machine, unspecified | `amt * machine_output_forming_benchmark / machine_output_forming` |
| output | waste mineral oil | `lube_forming` |

### deep drawing, steel, 650 kN press, single stroke | deep drawing, steel, 650 kN press, single stroke | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_forming / electricity_forming_benchmark` |
| input | lubricating oil | `lube_forming` |
| input | metal working machine, unspecified | `amt * machine_output_forming_benchmark / machine_output_forming` |
| output | waste mineral oil | `lube_forming` |

### energy and auxilliary inputs, metal working machine, with process heat from hard coal | energy and auxilliary inputs, metal working machine | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from hard coal | energy and auxilliary inputs, metal working machine | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from heavy fuel oil | energy and auxilliary inputs, metal working machine | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from heavy fuel oil | energy and auxilliary inputs, metal working machine | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from light fuel oil | energy and auxilliary inputs, metal working machine | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from light fuel oil | energy and auxilliary inputs, metal working machine | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from natural gas | energy and auxilliary inputs, metal working machine | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### energy and auxilliary inputs, metal working machine, with process heat from natural gas | energy and auxilliary inputs, metal working machine | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | electricity, low voltage | `amt * electricity_mwf / electricity_mwf_benchmark` |
| input | lubricating oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |
| output | waste mineral oil | `amt * lube_mwf / lube_mwf_benchmark * sump_life_benchmark / sump_life` |

### glider production, passenger car | glider, passenger car | Cutoff, U (Global)

| Direction | Flow | Formula |
|---|---|---|
| input | lubricating oil | `amt * lube_production / lube_production_benchmark` |

### internal combustion engine production, passenger car | internal combustion engine, passenger car | Cutoff, U (Global)

| Direction | Flow | Formula |
|---|---|---|
| input | lubricating oil | `amt * lube_production / lube_production_benchmark` |

### maintenance, passenger car | passenger car maintenance | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | lubricating oil | `amt * (oil_fill / drain_interval) / (oil_fill_benchmark / drain_interval_benchmark)` |
| output | waste mineral oil | `amt * (oil_fill / drain_interval) / (oil_fill_benchmark / drain_interval_benchmark)` |

### maintenance, passenger car | passenger car maintenance | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | lubricating oil | `amt * (oil_fill / drain_interval) / (oil_fill_benchmark / drain_interval_benchmark)` |
| output | waste mineral oil | `amt * (oil_fill / drain_interval) / (oil_fill_benchmark / drain_interval_benchmark)` |

### metal working, average for aluminium product manufacturing | metal working, average for aluminium product manufacturing | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for aluminium product manufacturing | metal working, average for aluminium product manufacturing | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for chromium steel product manufacturing | metal working, average for chromium steel product manufacturing | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for chromium steel product manufacturing | metal working, average for chromium steel product manufacturing | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for copper product manufacturing | metal working, average for copper product manufacturing | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for copper product manufacturing | metal working, average for copper product manufacturing | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for metal product manufacturing | metal working, average for metal product manufacturing | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for metal product manufacturing | metal working, average for metal product manufacturing | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for steel product manufacturing | metal working, average for steel product manufacturing | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### metal working, average for steel product manufacturing | metal working, average for steel product manufacturing | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | metal working machine, unspecified | `amt * machine_output_mwf_benchmark / machine_output_mwf` |

### transport, passenger, car, diesel, large size, EURO 3 | transport, passenger, car, diesel, large size, EURO 3 | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | diesel, low-sulfur | `amt * fuel_factor` |
| input | passenger car maintenance | `car_mass / (1240 * lifetime_ref)` |
| input | passenger car, diesel | `car_mass / lifetime_km` |
| output | Ammonia | `amt * fuel_factor` |
| output | Cadmium II | `amt * fuel_factor` |
| output | Carbon dioxide, fossil | `amt * fuel_factor` |
| output | Chromium III | `amt * fuel_factor` |
| output | Chromium VI | `amt * fuel_factor` |
| output | Copper ion | `amt * fuel_factor` |
| output | Dinitrogen monoxide | `amt * fuel_factor` |
| output | Lead II | `amt * fuel_factor` |
| output | Mercury II | `amt * fuel_factor` |
| output | Nickel II | `amt * fuel_factor` |
| output | PAH, polycyclic aromatic hydrocarbons | `amt * fuel_factor` |
| output | Selenium IV | `amt * fuel_factor` |
| output | Sulfur dioxide | `amt * fuel_factor` |
| output | Zinc II | `amt * fuel_factor` |

### transport, passenger, car, diesel, large size, EURO 3 | transport, passenger, car, diesel, large size, EURO 3 | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | diesel, low-sulfur | `amt * fuel_factor` |
| input | passenger car maintenance | `car_mass / (1240 * lifetime_ref)` |
| input | passenger car, diesel | `car_mass / lifetime_km` |
| output | Ammonia | `amt * fuel_factor` |
| output | Cadmium II | `amt * fuel_factor` |
| output | Carbon dioxide, fossil | `amt * fuel_factor` |
| output | Chromium III | `amt * fuel_factor` |
| output | Chromium VI | `amt * fuel_factor` |
| output | Copper ion | `amt * fuel_factor` |
| output | Dinitrogen monoxide | `amt * fuel_factor` |
| output | Lead II | `amt * fuel_factor` |
| output | Mercury II | `amt * fuel_factor` |
| output | Nickel II | `amt * fuel_factor` |
| output | PAH, polycyclic aromatic hydrocarbons | `amt * fuel_factor` |
| output | Selenium IV | `amt * fuel_factor` |
| output | Sulfur dioxide | `amt * fuel_factor` |
| output | Zinc II | `amt * fuel_factor` |

### transport, passenger, car, diesel, medium size, EURO 3 | transport, passenger, car, diesel, medium size, EURO 3 | Cutoff, U (Europe)

| Direction | Flow | Formula |
|---|---|---|
| input | diesel, low-sulfur | `amt * fuel_factor` |
| input | passenger car maintenance | `car_mass / (1240 * lifetime_ref)` |
| input | passenger car, diesel | `car_mass / lifetime_km` |
| output | Ammonia | `amt * fuel_factor` |
| output | Cadmium II | `amt * fuel_factor` |
| output | Carbon dioxide, fossil | `amt * fuel_factor` |
| output | Chromium III | `amt * fuel_factor` |
| output | Chromium VI | `amt * fuel_factor` |
| output | Copper ion | `amt * fuel_factor` |
| output | Dinitrogen monoxide | `amt * fuel_factor` |
| output | Lead II | `amt * fuel_factor` |
| output | Mercury II | `amt * fuel_factor` |
| output | Nickel II | `amt * fuel_factor` |
| output | PAH, polycyclic aromatic hydrocarbons | `amt * fuel_factor` |
| output | Selenium IV | `amt * fuel_factor` |
| output | Sulfur dioxide | `amt * fuel_factor` |
| output | Zinc II | `amt * fuel_factor` |

### transport, passenger, car, diesel, medium size, EURO 3 | transport, passenger, car, diesel, medium size, EURO 3 | Cutoff, U (Rest of World)

| Direction | Flow | Formula |
|---|---|---|
| input | diesel, low-sulfur | `amt * fuel_factor` |
| input | passenger car maintenance | `car_mass / (1240 * lifetime_ref)` |
| input | passenger car, diesel | `car_mass / lifetime_km` |
| output | Ammonia | `amt * fuel_factor` |
| output | Cadmium II | `amt * fuel_factor` |
| output | Carbon dioxide, fossil | `amt * fuel_factor` |
| output | Chromium III | `amt * fuel_factor` |
| output | Chromium VI | `amt * fuel_factor` |
| output | Copper ion | `amt * fuel_factor` |
| output | Dinitrogen monoxide | `amt * fuel_factor` |
| output | Lead II | `amt * fuel_factor` |
| output | Mercury II | `amt * fuel_factor` |
| output | Nickel II | `amt * fuel_factor` |
| output | PAH, polycyclic aromatic hydrocarbons | `amt * fuel_factor` |
| output | Selenium IV | `amt * fuel_factor` |
| output | Sulfur dioxide | `amt * fuel_factor` |
| output | Zinc II | `amt * fuel_factor` |

