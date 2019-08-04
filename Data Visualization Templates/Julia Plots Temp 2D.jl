using Plots; pyplot()
using LaTeXStrings

Plots.PyPlot.rc("text", usetex = "true")
Plots.PyPlot.rc("font", family = "CMU Serif")

X = range(-2pi, stop=2pi, length=100)
Y = 1.5 .* sin.(0.4 .+ 0.7X)

plot(dpi=256, gridls=:dash, legend=:topright, frame=:both,
     fgborder="#505050",fglegend="#A0A0A0", fgaxis="#505050", tickfontsize=10, legendfontsize=10)
plot!(X,Y, title = L"Title $\alpha$", lw=2, label=L"wave $f=f(x)$", annotation=(1, 1, L"Annotation $\beta$"))

png("a")