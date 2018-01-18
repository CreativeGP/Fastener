# coding: utf-8
"""A module written basic Fastener settings."""

bacon = {
    "scss": {
        ".*\.scss": [ "sass #f:#p#n.css" ]
    },
    "sass": {
        ".*\.sass": [ "sass #f:#p#n.css" ]
    },
    "web": {
        ".*\.scss": [ "sass #f:#p#n.css" ],
        ".*\.sass": [ "sass #f:#p#n.css" ],
        "[^_#\.].*\.pug": [ "pug #f" ],
    },
}
