import os,json
folder="wallpapers"
ext={".jpg",".jpeg",".png",".webp",".gif"}
items=[]
for root,dirs,files in os.walk(folder):
    for name in sorted(files):
        if os.path.splitext(name)[1].lower() in ext:
            rel=os.path.relpath(os.path.join(root,name),folder).replace("\\","/")
            parts=rel.split("/")
            category=parts[0] if len(parts)>1 else "Unsorted"
            title=os.path.splitext(parts[-1])[0].replace("_"," ").replace("-"," ").title()
            items.append({"file":rel,"title":title,"category":category})
with open("wallpapers.js","w",encoding="utf-8") as f:
    f.write("window.WALLPAPERS="+json.dumps(items,ensure_ascii=False,indent=2)+";")
print("Updated wallpaper list:",len(items))
