# launch-schedule-api

### Parses https://spaceflightnow.com/launch-schedule and returns JSON response with `mission name`, `launch vehicle` and `launch date`

### Response example:

```json
[
  {
    "mission": "Qilu 1 & Qilu 4",
    "launchVehicle": "Long March 6",
    "date": "April 26/27"
  },
  {
    "mission": "Starlink V1.0-L24",
    "launchVehicle": "Falcon 9",
    "date": "April 28/29"
  },
  {
    "mission": "Pléiades Neo 3",
    "launchVehicle": "Vega",
    "date": "April 28/29"
  }
]
```

### Install

```sh
git clone https://github.com/h4cktivist/launch-schedule-api.git
cd launch-schedule-api
pip install requirements.txt
```

### Run
```sh
python app.py
```
