mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
<<<<<<< HEAD
" > ~/.streamlit/config.toml 
=======
" > ~/.streamlit/config.toml
>>>>>>> fa89e2506872edba4f269e372f24b3959b2679a4
