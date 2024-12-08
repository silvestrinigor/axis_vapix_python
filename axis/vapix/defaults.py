from enum import Enum
class DevicePropertyType(Enum):
    ARCHITECTURE = "Architecture"
    BRAND = "Brand"
    BUILD_DATE = "BuildDate"
    HARDWARE_ID = "hardwareId"
    PROD_FULL_NAME = "ProdFullName"
    PROD_NBR = "ProdNbr"
    PROD_SHORT_NAME = "ProdShortName"
    PROD_TYPE = "ProdType"
    PROD_VARIANT = "ProdVariant"
    SERIAL_NUMBER = "SerialNumber"
    SOC = "Soc"
    SOC_SERIAL_NUMBER = "SocSerialNumber"
    VERSION = "Version"
    WEB_URL = "WebURL"
class MethodType(Enum):
    GET_PROPERTIES = "getProperties"
    GET_ALL_PROPERTIES = "getAllProperties"
    GET_ALL_UNRESTRICTED_PROPERTIES = "getAllUnrestrictedProperties"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    GET_API_LIST = "getApiList"
    ADD_IMAGE = "addImage"
    ADD_TEXT = "addText"
    LIST = "list"
    REMOVE = "remove"
    SET_IMAGE = "setImage"
    SET_TEXT = "setText"
    GET_OVERLAY_CAPABILITIES = "getOverlayCapabilities"
    GET_CAPTURE_MODES = "getCaptureModes"
    SET_CAPTURE_MODE = "setCaptureMode"
    GET_SERVICE_INFO = "getServiceInfo"
    GET_STATUS = "getStatus"
    START = "start"
    STOP = "stop"
    GET_DATE_TIME_INFO = "getDateTimeInfo"
    GET_ALL = "getAll"
    SET_DATE_TIME = "setDateTime"
    SET_TIME_ZONE = "setTimeZone"
    SET_POSIX_TIME_ZONE = "setPosixTimeZone"
    RESET_TIME_ZONE = "resetTimeZone"
class ApiPathType(Enum):
    AXIS_CGI_API_DISCOVERY = "axis-cgi/apidiscovery.cgi"
    AXIS_CGI_AUDIO_DEVICE_CONTROL = "axis-cgi/audiodevicecontrol.cgi"
    AXIS_CGI_AUDIO_TRANSMIT = "axis-cgi/audio/transmit.cgi"
    AXIS_CGI_AUDIO_RECEIVE = "axis-cgi/audio/receive.cgi"
    AXIS_CGI_BASIC_DEVICE_INFO = "axis-cgi/basicdeviceinfo.cgi"
    AXIS_CGI_CAPTURE_MODE = "axis-cgi/capturemode.cgi"
    AXIS_CGI_CLEAR_VIEW = "axis-cgi/clearviewcontrol.cgi"
    AXIS_CGI_DYNAMIC_OVERLAY = "axis-cgi/dynamicoverlay/dynamicoverlay.cgi"
    AXIS_CGI_FIND_MY_DEVICE = "axis-cgi/findmydevice.cgi"
    AXIS_CGI_FIRMWARE_MANAGEMENT = "axis-cgi/firmwaremanagement.cgi"
    AXIS_CGI_LEGACY_PARAMETER_HANDLING = "axis-cgi/param.cgi?action="
    AXIS_CGI_ADMIN_LEGACY_PARAMETER_HANDLING = "axis-cgi/admin/param.cgi?action="
    AXIS_CGI_NETWORK_SETTINGS = "axis-cgi/network_settings.cgi"
    AXIS_CGI_TIME = "axis-cgi/time.cgi"
    AXIS_CGI_APPLICATIONS_UPLOAD = "axis-cgi/applications/upload.cgi"
    AXIS_CGI_APPLICATIONS_CONTROL = "axis-cgi/applications/control.cgi?"
    AXIS_CGI_APPLICATIONS_CONFIG = "axis-cgi/applications/config.cgi?"
    AXIS_CGI_APPLICATIONS_LICENSE = "axis-cgi/applications/license.cgi?"
    AXIS_CGI_APPLICATIONS_LIST = "axis-cgi/applications/list.cgi"
    LOCAL_OBJECT_ANALYTICS = "local/objectanalytics/control.cgi"
    LOCAL_LOITERING_GUARD = "local/loiteringguard/control.cgi"
class ParamType(Enum):
    POSIX_TIME_ZONE = "posixTimeZone"
    ENABLE_DST = "enableDst"
    PROPERTY_LIST = "propertyList"
    CAMERA = "camera"
    TEXT = "text"
    POSITION = "position"
    TEXT_COLOR = "textColor"
    IDENTITY = "identity"
    OVERLAY_PATH = "overlayPath"
    FONT_SIZE = "fontSize"
    TEXT_BACK_GROUND_COLOR = "textBGColor"
    ID = "id"
    DURATION = "duration"
    DATE_TIME = "dateTime"
    TIME_ZONE = "timeZone"
class OverlayPositionType(Enum):
    BOTTOM_RIGHT = "bottomRight"
class OverlayColorType(Enum):
    WHITE = "white"
    RED = "red"
class TimeZoneType(Enum):
    EUROPE_STOCKHOLM = "Europe/Stockholm"
    EUROPE_LONDON = "Europe/London"
    EUROPE_PARIS = "Europe/Paris"
    AMERICA_NEW_YORK = "America/New_York"
    AMERICA_LOS_ANGELES = "America/Los_Angeles"
    ASIA_TOKYO = "Asia/Tokyo"
    ASIA_SINGAPORE = "Asia/Singapore"
    AUSTRALIA_SYDNEY = "Australia/Sydney"
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"
