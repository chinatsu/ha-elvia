"""The Elvia integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_API_KEY
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import ElviaApiClient
from .const import CONF_METERING_POINT_ID, CONF_TOKEN, DOMAIN, LOGGER, PLATFORMS
from .coordinator import ElviaDataUpdateCoordinator


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Elvia from a config entry."""

    hass.data.setdefault(DOMAIN, {})

    api = ElviaApiClient(
        api_key=entry.data[CONF_API_KEY],
        metering_point_id=entry.data[CONF_METERING_POINT_ID],
        token=entry.data[CONF_TOKEN],
        session=async_get_clientsession(hass),
    )

    data = await api.meteringpoint()


    coordinator = ElviaDataUpdateCoordinator(
        hass=hass,
        api=api,
        tariffType=data.gridTariff.tariffType,
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""

    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
