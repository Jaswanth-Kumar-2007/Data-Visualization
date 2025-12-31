# MatPlotLib

## Install in Computer

```python
pip install matplotlib
```

## Intialize MatplotLib

```python
import matplotlib.pyplot as plt
```

---

## List of PyPlot Functions

- plot
- bar
- boxplot
- hist
- pie
- scatter

i.e. plt.plot()

---

## List of Pyplot Functions to Customize plots

### grid

```python
plt.grid(True)
```

```bash
grid([b, which, axis])

b → True or False

which → "major", "minor", "both"

Major → main ticks

Minor → small ticks

axis → "x", "y", "both"
```

### legend

```python
plt.legend()
```

```bash
👉 Displays labels already attached to plots
```

### savefig

```python
plt.savefig("graph.png")
```

### show

```python
plt.show()
```

### title

```python
title(label[, fontdict, loc, pad])

plt.title("Sales Report")
```

### xlabel

```python
plt.xlabel("Year")
```

### xticks

```python
plt.xticks([0,1,2], ['A','B','C'])
👉 Changes tick positions and their names
```

```bash
Controls x-axis tick positions and text.
```

### ylabel

```python
plt.ylabel("Sales (Rs)")
```

### yticks

```python
plt.yticks([0,50,100], ['Low','Medium','High'])
```

---

### Kind for Different Plots

| kind    | Plot type                    |
|---------|------------------------------|
| line    | Line Plot (default)          |
| bar     | Vertical bar plot            |
| barh    | Horizontal bar plot          |
| hist    | Histogram                    |
| box     | Boxplot                      |
| area    | Area plot                    |
| pie     | Pie plot                     |
| scatter | Scatter plot                 |

---

Kinds have been Displayed in the [MatPlotLib](matplot.py) Section .
Kindly Refer there

---
