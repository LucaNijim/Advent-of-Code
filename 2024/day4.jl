using LinearAlgebra # for the diag function
data = 
    reshape(
        filter( 
            (x) -> x != '\n', 
            collect(Char, read("2024/input/input4"))
        ), 
        
        (:, countlines("2024/input/input4"))
    )


pt1 = 
    sum(
        length(
            collect(
                eachmatch(r"(XMAS|SAMX)", String(s), overlap=true)
            )
        ) # number of XMAS in each string, forwards or backwards

        for s in vcat( # applied to each 
            eachcol(data), # column 
            eachrow(data), # row
            [diag(data, i) for i in -size(data)[1]+1:size(data)[2]-1], # diagonal
            [diag(reverse(data, dims=1), i) 
                for i in -size(reverse(data, dims=1))[1]+1:size(reverse(data, dims=1))[2]-1
            ] # reverse diagonal 
        )
    ); # reverse diagonal

pt2 = 
    length(
        filter(
            (m) -> 
                all(
                    ss ∈ ["SAM", "MAS"] 
                    for ss ∈ 
                        String.(
                            diag.(
                                [m, reverse(m, dims=1)]
                            )
                        )
                ), # checks if a 3x3 submatrix is an X-MAS

            [data[i:i+2,j:j+2] 
                for i in 1:(size(data)[1]-2) 
                for j in 1:(size(data)[2]-2)
            ] # all 3x3 submatrices
        )
    );

println("Part 1 Solution: $pt1")
print("Part 2 Solution: $pt2")