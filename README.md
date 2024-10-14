# Elvia Grid Tariff for HomeAssistant

Forked from [sindrebroch/ha-elvia](https://github.com/sindrebroch/ha-elvia), go buy them a coffee if you want to.

![GitHub release (latest by date)](https://img.shields.io/github/v/release/chinatsu/ha-elvia?style=flat-square)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

HomeAssistant-integration for Elvia

## Notes and changes from sindrebroch's version

Firstly, the name of the integration has changed. 
There is a different [Elvia](https://www.home-assistant.io/integrations/elvia/) integration available, so to avoid shadowing its name I've chosen to call this one "Elvia Grid Tariff".

Secondly, I tentatively have not much interest in improving this integration beyond small fixes to keep it working through Home Assistant-upgrades; which was the initial spark to fork this to begin with.
I'm happy to receive help through PRs and issues to improve the integration though, and maybe that'll motivate me to improve it too.
Ideally, sindrebroch returns at some point to merge the changes proposed already, then I'll probably delete this fork.

If others want to contribute to this, I could also transfer this to a GitHub organization to more easily manage maintainers and such, but we'll cross that bridge if we get there.

## Requirements

- Metering point id. (Målepunkt-ID, not Målernummer) Log into [Elvia](https://www.elvia.no/minside) and find your ID.
- API-key. Sign up for GridTariffAPI at the [Elvia developer portal](https://developers.elvia.no/). You may retreive the API key in your [profile](https://developers.elvia.no/profile) (the primary key should be sufficient).
- Token. [Read how](https://www.elvia.no/smart-forbruk/api-er-for-smartere-hjem-og-bedrifter/slik-kan-du-ta-i-bruk-metervalue-api/).
   - The short of it is: log into [Elvia](https://www.elvia.no/minside), under "Andre tjenester" select "Tilganger".
   - From there, select "Opprett token for målerverdier i API".

## Installation

### HACS (Recommended)

1. Ensure that [HACS](https://hacs.xyz/) is installed.
2. Add this repository as a custom repository
3. Search for and install the "Elvia Grid Tariff" integration.
4. Restart Home Assistant.
5. Add the `Elvia Grid Tariff` integration to Home Assistant from the Integrations page

### Manual installation

1. Download the `Source code (zip)` file from the [latest release](https://github.com/chinatsu/ha-elvia/releases/latest).
2. Unpack the release and copy the `custom_components/elvia_grid_tariff` directory into the `custom_components` directory of your Home Assistant installation.
3. Restart Home Assistant.
4. Add the `Elvia Grid Tariff` integration to HA from the integration-page


## Sensors
- Energy price
   - Daily tariff (array of hourly values for the day)
- Fixed price hourly
- Fixed price level
- Fixed price monthly
- Average max
   - Current month
   - Previous month
- Max hours [1, 2, 3]
   - Current month
      - StartTime (attribute)
      - EndTime (attribute)
   - Previous month
      - StartTime (attribute)
      - EndTime (attribute)

## Debugging
If something is not working properly, logs might help with debugging. To turn on debug-logging add this to your `configuration.yaml`
```
logger:
  default: info
  logs:
    custom_components.elvia: debug
```

## API limitations
Limited to 200 calls/hour/user. The integration normally polls once every hour.

## Inspiration
https://github.com/uphillbattle/NettleieElvia
