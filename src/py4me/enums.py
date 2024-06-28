from enum import Enum


class Currency(str, Enum):
    aed = 'aed'  # United Arab Emirates Dirham
    ars = 'ars'  # Argentine Peso
    aud = 'aud'  # Australian Dollar
    brl = 'brl'  # Brazilian Real
    btc = 'btc'  # Bitcoin
    cad = 'cad'  # Canadian Dollar
    chf = 'chf'  # Swiss Franc
    cny = 'cny'  # Chinese Yuan
    cop = 'cop'  # Colombian Peso
    czk = 'czk'  # Czech Koruna
    dkk = 'dkk'  # Danish Krone
    dzd = 'dzd'  # Algerian Dinar
    euro = 'euro'  # Euro
    gbp = 'gbp'  # British Pound
    hkd = 'hkd'  # Hong Kong Dollar
    huf = 'huf'  # Hungarian Forint
    idr = 'idr'  # Indonesian Rupiah
    ils = 'ils'  # Israeli New Shekel
    inr = 'inr'  # Indian Rupee
    jpy = 'jpy'  # Japanese Yen
    krw = 'krw'  # Korean Won
    mxn = 'mxn'  # Mexican Peso
    ngn = 'ngn'  # Nigerian Naira
    nok = 'nok'  # Norwegian Krone
    nzd = 'nzd'  # New Zealand Dollar
    omr = 'omr'  # Omani Rial
    pkr = 'pkr'  # Pakistani Rupee
    php = 'php'  # Philippine Peso
    pln = 'pln'  # Polish Zloty
    rub = 'rub'  # Russian Ruble
    sek = 'sek'  # Swedish Krona
    sgd = 'sgd'  # Singapore Dollar
    thb = 'thb'  # Thai Baht
    try_ = 'try'  # Turkish Lira
    twd = 'twd'  # New Taiwan Dollar
    usd = 'usd'  # US Dollar
    zar = 'zar'  # South African Rand


class Plan(str, Enum):
    basic = 'basic'
    premium = 'premium'
    premium_plus = 'premium_plus'


class Locale(str, Enum):
    enUS = 'en-US'  # English (United States)
    enGB = 'en-GB'  # English (United Kingdom)
    nl = 'nl'  # Dutch
    de = 'de'  # German
    fr = 'fr'  # French
    es = 'es'  # Spanish
    esAR = 'es-AR'  # Spanish (Argentina)
    esES = 'es-ES'  # Spanish (Spain)
    eu = 'eu'  # Basque
    ptPT = 'pt-PT'  # Portuguese (Portugal)
    ptBR = 'pt-BR'  # Portuguese (Brazil)
    it = 'it'  # Italian
    da = 'da'  # Danish
    ga = 'ga'  # Irish
    cy = 'cy'  # Welsh
    fi = 'fi'  # Finnish
    nb = 'nb'  # Norwegian
    sv = 'sv'  # Swedish
    is_ = 'is'  # Icelandic
    pl = 'pl'  # Polish
    cs = 'cs'  # Czech
    el = 'el'  # Greek
    ro = 'ro'  # Romanian
    hu = 'hu'  # Hungarian
    sk = 'sk'  # Slovak
    tr = 'tr'  # Turkish
    ru = 'ru'  # Russian
    uk = 'uk'  # Ukrainian
    et = 'et'  # Estonian
    ar = 'ar'  # Arabic
    zhCN = 'zh-CN'  # Chinese (Simplified)
    zhTW = 'zh-TW'  # Chinese (Traditional)
    ja = 'ja'  # Japanese
    ko = 'ko'  # Korean
    id_ = 'id'  # Indonesian
    th = 'th'  # Thai
    vi = 'vi'  # Vietnamese
    ms = 'ms'  # Malay
    fa = 'fa'  # Persian
    he = 'he'  # Hebrew
    hi = 'hi'  # Hindi
    af = 'af'  # Afrikaans
    am = 'am'  # Amharic
    az = 'az'  # Azerbaijani
    bs = 'bs'  # Bosnian
    hr = 'hr'  # Croatian
    faAF = 'fa-AF'  # Dari
    frCA = 'fr-CA'  # French (Canada)
    ka = 'ka'  # Georgian
    lv = 'lv'  # Latvian
    lt = 'lt'  # Lithuanian
    sr = 'sr'  # Serbian
    sr_latin = 'sr@Latin'  # Serbian (Latin)
    sl = 'sl'  # Slovenian
    ta = 'ta'  # Tamil
    mk = 'mk'  # Macedonia


class AddressLabel(str, Enum):
    home = 'home'
    mailing = 'mailing'

