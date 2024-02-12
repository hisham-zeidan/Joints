import ghpythonlib.components as gh

def create_joint(x, y):
    edge_1 = gh.DeconstructBrep(y)[1][1]
    edge_2 = gh.DeconstructBrep(y)[1][5]
    midpoint_1 = gh.CurveMiddle(edge_1)
    midpoint_2 = gh.CurveMiddle(edge_2)

    # Calculate scaling factor based on x width and desired height
    x_width = gh.Curve.GetLength(gh.DeconstructBrep(x)[1][4].ToNurbsCurve())
    init_height = gh.Curve.GetLength(edge_1.ToNurbsCurve())
    scaleFactor = x_width / init_height

    scaled_geo_1 = gh.Scale(y, midpoint_1, scaleFactor)
    scaled_geo_2 = gh.Scale(y, midpoint_2, scaleFactor)

    f = gh.SolidDifference(y, scaled_geo_1[0])
    Pcs2 = gh.SolidDifference(f, scaled_geo_2[0])
    Pcs1 = gh.SolidDifference(x, Pcs2)

    return [Pcs1, Pcs2]

def run_script(x, y, **kwargs):
    brep1 = x  # Connect a brep 1
    brep2 = y  # Connect a brep 2

    output = create_joint(brep1, brep2)
    return {"a": output}