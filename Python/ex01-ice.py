#!/usr/bin/env python3

from Icestudio import Ice

ice = Ice()
ice.open_file("../Test-files/test-01-info.ice")
print(ice)