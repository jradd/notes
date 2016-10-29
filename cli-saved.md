# Command—line and Script Snippets
Worth saving


# awk  

`awk 'NF{i++} END { print "," i }' foo.txt`

# sed


## files

files with fewest count of lines (100cnt)
`find ./ -type f -name '*.md' -print0 -exec awk 'NF{i++} END { print "," i }' {} \; |sort -t, -nk2
|head -n100`


### curl
Use curl to update local copy of a file if the remote copy is newer than our local copy

We accomplish this with the `curl -z <time-cond>` argument. Neat!

```bash
for f in $(curl -fk -L https://live.sysinternals.com/tools/ |egrep -o '>[aA0-zZ9]*.(exe|chm)<'); do f="$(echo "${f}" |cut -c 2- |sed -e 's|<||g')"; curl -fksSR -z "./${f}" -O "https://live.sysinternals.com/tools/${f}"; done
```   

