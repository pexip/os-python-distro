#!/usr/bin/python3

import distro

# Not the full API, but enough to flex the package.
print(distro.id())
print(distro.name())
print(distro.name(pretty=True))
print(distro.version())
print(distro.version(pretty=True))
print(distro.info())

# Use lsb_release for enhanced information.
assert len(distro.lsb_release_info()) > 0, (
    "Why isn't lsb_release(1) available?")
