import ghpythonlib.components as gh

print('inputs:x(brep),y(brep) OutPut: OutPut')
edge_1 = gh.DeconstructBrep(y)[1][1]
edge_2 = gh.DeconstructBrep(y)[1][5]
midpoint_1 = gh.CurveMiddle(edge_1)
midpoint_2 = gh.CurveMiddle(edge_2)

# Calculate scaling factor based on x width and desired height
x_width = gh.Length(gh.DeconstructBrep(x)[1][4])
init_height = gh.Length(edge_1)
scaleFactor = x_width /init_height 

scaled_geo_1 = gh.Scale(y, midpoint_1, scaleFactor)
scaled_geo_2 = gh.Scale(y, midpoint_2, scaleFactor)

f = gh.SolidDifference(y, scaled_geo_1[0])
Pcs2 = gh.SolidDifference(f, scaled_geo_2[0])
Pcs1 = gh.SolidDifference(x, Pcs2)
OutPut = Pcs1,Pcs2
