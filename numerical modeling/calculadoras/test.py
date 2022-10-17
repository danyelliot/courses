import speedtest
st = speedtest.Speedtest()
ds = st.download()
us = st.upload()
print("Download Speed: ", ds)
print("Upload Speed: ", us)

