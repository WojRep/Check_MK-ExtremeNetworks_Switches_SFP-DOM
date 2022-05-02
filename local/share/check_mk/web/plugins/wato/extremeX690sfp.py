#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

group = "datasource_programs"

register_rule(group,
              "special_agents:extremeX690sfp",
              Dictionary(
                  elements=[
                      ("user",
                       TextAscii(
                           title=_("Username"),
                       )
                       ),
                      ("password",
                       Password(
                           title=_("Password"),
                       )
                       ),
                      ("port",
                       Transform(
                           ListChoice(
                               choices=[
                                   ("1",   _("Port 1")),
                                   ("2",   _("Port 2")),
                                   ("3",   _("Port 3")),
                                   ("4",   _("Port 4")),
                                   ("5",   _("Port 5")),
                                   ("6",   _("Port 6")),
                                   ("7",   _("Port 7")),
                                   ("8",   _("Port 8")),
                                   ("9",   _("Port 9")),
                                   ("10",   _("Port 10")),
                                   ("11",   _("Port 11")),
                                   ("12",   _("Port 12")),
                                   ("13",   _("Port 13")),
                                   ("14",   _("Port 14")),
                                   ("15",   _("Port 15")),
                                   ("16",   _("Port 16")),
                                   ("17",   _("Port 17")),
                                   ("18",   _("Port 18")),
                                   ("19",   _("Port 19")),
                                   ("20",   _("Port 20")),
                                   ("21",   _("Port 21")),
                                   ("22",   _("Port 22")),
                                   ("23",   _("Port 23")),
                                   ("24",   _("Port 24")),
                                   ("25",   _("Port 25")),
                                   ("26",   _("Port 26")),
                                   ("27",   _("Port 27")),
                                   ("28",   _("Port 28")),
                                   ("29",   _("Port 29")),
                                   ("30",   _("Port 30")),
                                   ("31",   _("Port 31")),
                                   ("32",   _("Port 32")),
                                   ("33",   _("Port 33")),
                                   ("34",   _("Port 34")),
                                   ("35",   _("Port 35")),
                                   ("36",   _("Port 36")),
                                   ("37",   _("Port 37")),
                                   ("38",   _("Port 38")),
                                   ("39",   _("Port 39")),
                                   ("40",   _("Port 40")),
                                   ("41",   _("Port 41")),
                                   ("42",   _("Port 42")),
                                   ("43",   _("Port 43")),
                                   ("44",   _("Port 44")),
                                   ("45",   _("Port 45")),
                                   ("46",   _("Port 46")),
                                   ("47",   _("Port 47")),
                                   ("48",   _("Port 48")),
                                   ("49",   _("Port 49")),
                                   ("50",   _("Port 50")),
                                   ("51",   _("Port 51")),
                                   ("52",   _("Port 52")),
                                   ("53",   _("Port 53")),
                                   ("54",   _("Port 54")),
                                   ("55",   _("Port 55")),
                                   ("56",   _("Port 56")),
                                   ("57",   _("Port 57")),
                                   ("58",   _("Port 58")),
                                   ("59",   _("Port 59")),
                                   ("60",   _("Port 60")),
                                   ("61",   _("Port 61")),
                                   ("62",   _("Port 62")),
                                   ("63",   _("Port 63")),
                                   ("64",   _("Port 64")),

                               ],
                               default_value=[],
                           ),
                           title=_("Select ports ..."),
                       )
                       ),
                  ],
                  optional_keys=False
              ),
              title=_("Extreme X690 SFP+ parameters via jsonrpc"),
              help=_("This rule activates an agent that collects information from "
                     "Extreme X690 SFP+ interface."),
              match='all')

register_check_parameters(
    subgroup_networking,
    'extremeX690sfp',
    _('Extreme X690 SFP/SFP+'),
    Transform(
        Dictionary(
            title=_('Extreme X690 SFP/SFP+ Params'),
            elements=[
                ('rx', Tuple(
                    title=_('SFP/SFP+ Rx Signal'),
                    elements=[
                        Float(title=_('Warning at'), unit='dBm',
                              default_value='-10'
                              ),
                        Float(title=_('Critical at'), unit='dBm',
                              default_value='-14'
                              ),
                    ])),
                ('temp', Tuple(
                    title=_('SFP/SFP+ Temperature'),
                    elements=[
                        Float(title=_('Warning at'), unit='st.C',
                              default_value='65.0'
                              ),
                        Float(title=_('Critical at'), unit='st.C',
                              default_value='75.0'
                              ),
                    ])),
            ], default_value=['rx']
        ),
        forth=lambda old: type(old) != dict and {"rx": old} or old,
    ),
    TextAscii(
        title=_("Extreme X690 SFP/SFP+"),
    ),
    match_type='dict',
)