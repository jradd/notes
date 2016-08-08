# Package Management Notes
(Primarily APT on Debian)


`dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n`


### Cleanup Configs
`dpkg --list | grep '^rcb'`

`dpkg --list | grep '^rcb' | awk '{ print $2 }' | xargs dpkg -P`


### Query
Find packages installed by another package that recommends it.

`aptitude search '?and( ?automatic(?reverse-recommends(?installed)), ?not(?automatic(?reverse-depends(?installed))) )'`

To remove them, just pipe to awk:
`... | awk '{ print $3 }' | xargs dpkg -P`

