# Visual representation of some operators of fuzzy logic

To run it you'll need matplotlib.
You can setup a virtual environment inside the project folder with

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

The two values that can be easily adjusted in the code are `TILES` and `COLOR_MAP`.
- Increasing or decreasing the value of `TILES` makes the figure more or less fine-grained.
- Possible values to assign to `COLOR_MAP` can be found in this 
[colormap reference](https://matplotlib.org/users/colormaps.html#grayscale-conversion).

## Intersection
![Minimum](images/intersection_minimum.png)
![Average](images/intersection_average.png)
![Product](images/intersection_product.png)
![Limited difference](images/intersection_limited_difference.png)
![Drastic intersection](images/intersection_drastic_intersection.png)

## Union
![Maximum](images/union_maximum.png)
![Average](images/union_average.png)
![Algebraic sum](images/union_algebraic_sum.png)
![Boundary sum](images/union_boundary_sum.png)
![Drastic union](images/union_drastic_union.png)

## Inference
![Gaines](images/inference_gaines.png)
![Godel](images/inference_godel.png)
![Goguen](images/inference_goguen.png)
![Kleene](images/inference_kleene.png)
![Reichenbach](images/inference_reichenbach.png)
![Klir-Yuan](images/inference_klir-yuan.png)
![Zadeh](images/inference_zadeh.png)
![Lukasiewicz](images/inference_lukasiewicz.png)
