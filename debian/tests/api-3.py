#!/usr/bin/python3

import distro


# Not the full API, but enough to flex the package.
print(distro.linux_distribution())
print(distro.linux_distribution(full_distribution_name=False))
print(distro.name())
print(distro.name(pretty=True))

# Use lsb_release for enhanced information.
assert len(distro.LinuxDistribution().lsb_release_info()) > 0, (
    "Why isn't lsb_release(1) available?")
