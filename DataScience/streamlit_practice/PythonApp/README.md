## Python Streamlit App

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

1. install reqs: ```pip install -r requirements.txt```
2. Run app: ```streamlit run app.py```
3. access app on: http://localhost:8501


### Troubleshooting

If this error occurs:
```
raise RuntimeError('Not supported on 32-bit Windows')
RuntimeError: Not supported on 32-bit Windows
----------------------------------------
ERROR: Failed building wheel for pyarrow
```

try : ```pip install streamlit==0.62```

## Resources
- https://docs.streamlit.io/en/stable/
- https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020