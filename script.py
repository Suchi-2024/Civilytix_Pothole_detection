import os, random, shutil

IMAGE_DIR = "dataset/Images"
LABEL_DIR = "dataset/Labels"
OUTPUT_DIR = "dataset/"

train_ratio = 0.75

# create folders
for split in ["train", "val"]:
    os.makedirs(os.path.join(OUTPUT_DIR, "Images", split), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "Labels", split), exist_ok=True)

# shuffle and split
images = [f for f in os.listdir(IMAGE_DIR) if f.endswith((".jpg",".png"))]
random.shuffle(images)
split_idx = int(len(images) * train_ratio)

train_imgs = images[:split_idx]
val_imgs = images[split_idx:]

def move(imgs, split):
    for img in imgs:
        # image
        shutil.copy2(os.path.join(IMAGE_DIR, img), os.path.join(OUTPUT_DIR, "Images", split, img))
        # label
        label = os.path.splitext(img)[0] + ".txt"
        src = os.path.join(LABEL_DIR, label)
        dst = os.path.join(OUTPUT_DIR, "Labels", split, label)
        if os.path.exists(src):
            shutil.copy2(src, dst)
        else:
            open(dst, "w").close()  # empty label file

move(train_imgs, "train")
move(val_imgs, "val")
