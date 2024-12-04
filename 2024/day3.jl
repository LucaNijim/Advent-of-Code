s = "do()"*read("2024/input/input3", String)*"don't()"

pt1(st::String) = 
    sum(
        parse(Int, mul[:n1])*parse(Int,mul[:n2]) 
        for mul in eachmatch(r"mul\((?<n1>[0-9]+),(?<n2>[0-9]+)\)", st)
    )
pt2(st::String) = 
    occursin(r"do\(\)", st) ? 
        pt1(st[match(r"do\(\)", st).offset:match(r"do\(\)", st).offset+match(r"don't\(\)", st[match(r"do\(\)", st).offset:end]).offset+5])+ pt2(st[match(r"do\(\)", st).offset+match(r"don't\(\)", st[match(r"do\(\)", st).offset:end]).offset+5:end]) : 0

print("Part 1 Solution: ")
println(pt1(s))
print("Part 2 Solution: ")
println(pt2(s))