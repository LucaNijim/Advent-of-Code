s = "do()"*read("2024/input/input3", String)*"don't()"

pt1(st::String) = 
    sum(
        parse(Int, mul[:n1])*parse(Int,mul[:n2]) 
        for mul in eachmatch(r"mul\((?<n1>[0-9]+),(?<n2>[0-9]+)\)", st)
    )

function pt2(st::String)
    if !occursin(r"do\(\)", st)
        return 0
    end 
    doloc = match(r"do\(\)", st).offset
    dontloc = match(r"don't\(\)", st[doloc:end]).offset + doloc + 5
    return pt1(st[doloc:dontloc]) + pt2(st[dontloc:end])
end

print("Part 1 Solution: ")
println(pt1(s))
print("Part 2 Solution: ")
println(pt2(s))