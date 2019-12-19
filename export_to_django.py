import sys, os, glob
from shutil import copy

def build(package):
    print(package)

    old_files = glob.glob("../static/"+package+"/css/*")
    old_files += glob.glob("../static/"+package+"/js/*")
    for f in old_files:
        os.remove(f)

    css_files = glob.glob("dist/static/css/*")
    for f in css_files:
        name = f.split("/")[-1]
        copy(f, "../static/"+package+"/css/")

    js_files = glob.glob("dist/static/js/*")
    for f in js_files:
        name = f.split("/")[-1]
        copy(f, "../static/"+package+"/js/")

    h = open("dist/index.html")
    html = h.read()
    h.close()

    h = open("../guns/templates/"+package+".html")
    main_html = h.read()
    h.close()

    t = html.split("/static/js/manifest.")[1].split(".js")[0]
    old_t = main_html.split("js/manifest.")[1].split(".js")[0]
    main_html = main_html.replace(old_t, t)

    t = html.split("/static/js/vendor.")[1].split(".js")[0]
    old_t = main_html.split("js/vendor.")[1].split(".js")[0]
    main_html = main_html.replace(old_t, t)

    t = html.split("/static/js/app.")[1].split(".js")[0]
    old_t = main_html.split("js/app.")[1].split(".js")[0]
    main_html = main_html.replace(old_t, t)

    t = html.split("/static/css/app.")[1].split(".css")[0]
    old_t = main_html.split("css/app.")[1].split(".css")[0]
    main_html = main_html.replace(old_t, t)

    h = open("../guns/templates/"+package+".html", "w")
    h.write(main_html)
    h.close()

    print("Done Done Done")

if __name__ == "__main__":
    args = sys.argv
    build(args[1])
    