from requests import Request
import urllib.parse
import urllib
import io
import json
from datetime import datetime
from packaging.version import Version
from .types import ApiPathType, RequestMethod, MethodType, DevicePropertyType, ParamType, FirmwareUpgradeType, RequestUrlParamType, FactoryDefaultModeType, AutoCommitType, RequestParamType, ActionType, ContentType, TimeZoneType
from .defaults import AxisDevice, ImageOverlay, TextOverlay, NetworkResolverConfiguration, IPv4AddressConfiguration, HostnameConfiguration, NTPClientConfiguration
from .utils import serialize_datetime

def get_supported_versions_request(device: AxisDevice, api: ApiPathType, context: str | None = None):
    request_body = {}
    request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
    if context != None: request_body[RequestParamType.CONTEXT.value] = context
    return Request("POST", device.base_url + api.value, json=request_body, auth=device.auth)

def get_properties_request(device: AxisDevice, properties: list[DevicePropertyType], api_version: Version, context: str | None = None):
    params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
    request_body = {}
    request_body[RequestParamType.API_VERSION.value] = api_version
    request_body[RequestParamType.METHOD.value] = MethodType.GET_PROPERTIES.value
    request_body[RequestParamType.PARAMS.value] = params
    if context != None: request_body[RequestParamType.CONTEXT.value] = context 
    return Request("POST", device.base_url + ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO.value, auth=device.auth)

def get_all_properties_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body = {}
    request_body[RequestParamType.API_VERSION.value] = api_version
    request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_PROPERTIES.value
    if context != None: request_body[RequestParamType.CONTEXT.value] = context 
    return Request("POST", device.base_url + ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO.value, auth=device.auth)


"""
def get_all_unrestricted_properties_request(device: AxisDevice, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.GET_ALL_UNRESTRICTED_PROPERTIES)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_api_list_request(device: AxisDevice, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_API_DISCOVERY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.GET_API_LIST)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build    

def add_dynamic_overlay_image_request(device: AxisDevice, api_version: Version, image_overlay: ImageOverlay, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.ADD_IMAGE)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, image_overlay.get_all_params())
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def add_dynamic_overlay_text_request(device: AxisDevice, api_version: Version, text_overlay: TextOverlay, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.ADD_TEXT)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, text_overlay.get_all_params())
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def list_overlays_request(device: AxisDevice, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.LIST)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, {})
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_dynamic_overlay_text_request(device: AxisDevice, api_version: Version, text_overlay: TextOverlay, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.SET_TEXT)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, text_overlay.get_all_params())
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_dynamic_overlay_image_request(device: AxisDevice, api_version: Version, image_overlay: ImageOverlay, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.SET_IMAGE)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, image_overlay.get_all_params())
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def remove_dynamic_overlay_request(device: AxisDevice, api_version: Version, identity: int, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.REMOVE)
    request_body_class.add_or_set_method_params(ParamType.IDENTITY, identity)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_dynamic_overlay_capabilities_request(device: AxisDevice, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.GET_OVERLAY_CAPABILITIES)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_capture_modes_request(device: AxisDevice, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_CAPTURE_MODE.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.GET_CAPTURE_MODES)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_capture_mode_request(device: AxisDevice, channel: int, capture_mode_id: int, api_version: Version, context: str | None = None):
    url = device.url + ApiPathType.AXIS_CGI_CAPTURE_MODE.value
    request_body_class = AxisRequestBody()
    request_body_class.add_or_set_context(context)
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_method(MethodType.SET_CAPTURE_MODE)
    request_body_class.add_or_set_request_param(RequestParamType.CAPTURE_MODE_ID, capture_mode_id)
    request_body_class.add_or_set_request_param(RequestParamType.CHANNEL, channel)
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_clear_view_service_info_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_SERVICE_INFO)
    url = device.url + ApiPathType.AXIS_CGI_CLEAR_VIEW.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def start_cleaning_view_request(device: AxisDevice, api_version: Version, id: int, duration: int = None, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.START)
    request_body_class.add_or_set_method_params(ParamType.ID, id)
    request_body_class.add_or_set_method_params(ParamType.DURATION, duration)
    url = device.url + ApiPathType.AXIS_CGI_CLEAR_VIEW.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def stop_cleaning_view_request(device: AxisDevice, api_version: Version, id: int, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.STOP)
    request_body_class.add_or_set_method_params(ParamType.ID, id)
    url = device.url + ApiPathType.AXIS_CGI_CLEAR_VIEW.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_cleaning_view_status_request(device: AxisDevice, api_version: Version, id: int, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_STATUS)
    request_body_class.add_or_set_method_params(ParamType.ID, id)
    url = device.url + ApiPathType.AXIS_CGI_CLEAR_VIEW.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_date_time_info_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_DATE_TIME_INFO)
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_all_date_time_api_info_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_ALL)
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_date_time_request(device: AxisDevice, api_version: Version, date_time: datetime, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_DATE_TIME)
    request_body_class.add_or_set_method_params(ParamType.DATE_TIME, serialize_datetime(date_time))
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_time_zone_request(device: AxisDevice, api_version: Version, time_zone: TimeZoneType, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_TIME_ZONE)
    request_body_class.add_or_set_method_params(ParamType.TIME_ZONE, time_zone.value)
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_posix_time_zone_request(device: AxisDevice, api_version: Version, posix_time_zone: str, enable_dst: bool, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_POSIX_TIME_ZONE)
    request_body_class.add_or_set_method_params(ParamType.POSIX_TIME_ZONE, posix_time_zone)
    request_body_class.add_or_set_method_params(ParamType.ENABLE_DST, enable_dst)
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def reset_time_zone_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.RESET_TIME_ZONE)
    url = device.url + ApiPathType.AXIS_CGI_TIME.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_ntp_info_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_NTP_INFO)
    url = device.url + ApiPathType.AXIS_CGI_NTP.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_ntp_client_configuration_request(device: AxisDevice, api_version: Version, configuration: NTPClientConfiguration, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_NTP_CLIENT_CONFIGURATION)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, configuration.get_all_params())
    url = device.url + ApiPathType.AXIS_CGI_NTP.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_network_info_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.GET_NETWORK_INFO)
    url = device.url + ApiPathType.AXIS_CGI_NETWORK_SETTINGS.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_network_hostname_request(device: AxisDevice, api_version: Version, configuration: HostnameConfiguration, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_HOSTNAME_CONFIGURATION)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, configuration.get_all_params())
    url = device.url + ApiPathType.AXIS_CGI_NETWORK_SETTINGS.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_network_ipv4_address_request(device: AxisDevice, api_version: Version, configuration: IPv4AddressConfiguration, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_IPV4_ADDRESS_CONFIGURATION)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, configuration.get_all_params())
    url = device.url + ApiPathType.AXIS_CGI_NETWORK_SETTINGS.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_network_resolver_request(device: AxisDevice, api_version: Version, configuration: NetworkResolverConfiguration, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.SET_RESOLVER_CONFIGURATION)
    request_body_class.add_or_set_request_param(RequestParamType.PARAMS, configuration.get_all_params())
    url = device.url + ApiPathType.AXIS_CGI_NETWORK_SETTINGS.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def get_firmware_status_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.STATUS)
    url = device.url + ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_firmware_rollback_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.ROLLBACK)
    url = device.url + ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_firmware_factory_default_request(device: AxisDevice, mode: FactoryDefaultModeType, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.FACTORY_DEFAULT)
    request_body_class.add_or_set_method_params(ParamType.FACTORY_DEFAULT_MODE, mode.value)
    url = device.url + ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def set_firmware_reboot_request(device: AxisDevice, api_version: Version, context: str | None = None):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.REBOOT)
    url = device.url + ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_json(request_body_class.get_request_body())
    return request_build

def upgrade_firmware_system_settings_request(device: AxisDevice, file_name: str, file_obj: io.BufferedReader,  type: FirmwareUpgradeType = FirmwareUpgradeType.NORMAL):
    url = device.url + ApiPathType.AXIS_CGI_SYSTEM_SETTINGS_FIRMWARE_UPGRADE.value + RequestUrlParamType.TYPE.value + type.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_files({file_name: file_obj})
    return request_build

def upgrade_firmware_request(device: AxisDevice, file_obj: io.BufferedReader, api_version: Version, context: str | None = None, auto_rool_back = None, factory_default_mode: FactoryDefaultModeType = FactoryDefaultModeType.NONE, auto_commit: AutoCommitType = AutoCommitType.NONE):
    request_body_class = AxisRequestBody()
    request_body_class.add__or_set_api_version(api_version=api_version)
    request_body_class.add_or_set_context(context)
    request_body_class.add_or_set_method(MethodType.UPGRADE)
    request_body_class.add_or_set_method_params(ParamType.AUTO_ROLLBACK, auto_rool_back)
    request_body_class.add_or_set_method_params(ParamType.FACTORY_DEFAULT_MODE, factory_default_mode.value)
    request_body_class.add_or_set_method_params(ParamType.AUTO_COMMIT, auto_commit.value)
    url = device.url + ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT.value
    request_build = RequestBuilder(method=RequestMethod.POST, url=url)
    request_build.set_data({'data': json.dumps((request_body_class.get_request_body()))})
    request_build.set_files({'file': ('firmware_file.bin', file_obj, ContentType.APPLICATION_OCTETSTREAM.value)})
    return request_build

def param_handle_request(device: AxisDevice, action: ActionType, **keyargs):
    url = device.url + ApiPathType.AXIS_CGI_PARAM.value + RequestUrlParamType.ACTION.value + action.value
    if keyargs:
        encoded_params = urllib.parse.urlencode(keyargs)
        url = f"{url}&{encoded_params}"
    if action == ActionType.LIST:
        request_build = RequestBuilder(RequestMethod.GET, url)
    else:
        request_build = RequestBuilder(RequestMethod.POST, url)
    return request_build
"""