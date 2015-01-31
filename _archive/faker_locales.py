#!/usr/bin/env python

locale = ["bg_BG", "cs_CZ", "de_DE", "dk_DK", "el_GR",\
        "en_CA", "en_GB", "en_US", "es_ES", "es_MX",\
        "fa_IR", "fi_FI", "fr_FR", "hi_IN", "it_IT",\
        "ko_KR", "lt_LT", "lv_LV", "nl_NL", "pl_PL",\
        "pt_BR", "ru_RU", "sl_SI", "zh_CN", "zh_TW"]

print "Number of locales: ", len(locale)
print "Locale 1: ", locale[1]
print "All locales: ", locale
for i in locale:
    print i
print "locale pop: ", locale.pop()
