import os
import re

# Paths
BLOG_POSTS_PATH = "/Users/Privat/Projects/myWebsite/Blog/content/post/"

# Step 1: Process each markdown file in the posts directory
filenames = [filename for filename in os.listdir(BLOG_POSTS_PATH) if not filename.startswith(".")]

for filename in filenames:
    filepath = os.path.join(BLOG_POSTS_PATH, filename)
    files = os.listdir(filepath)
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(filepath, file), "r") as f:
                content = f.read()

            # Step 2: Find all image links in the format ![Image Description](Pasted%20image%20...%20.png)
            images = re.findall(r'\[\[([^]]*\.(?:jpeg|jpg|png|gif|bmp|webp))\]\]', content)
            
            # Step 3: Replace image links and ensure URLs are correctly formatted
            for image in images:
                # Prepare the Markdown-compatible link with %20 replacing spaces
                image_name = os.path.split(image)[-1]
                markdown_image = f"[Image Description]({image_name.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)


            # Step 5: Write the updated content back to the markdown file
            if file not in "index.md":
                os.remove(os.path.join(filepath, file))
                print("renaming file")
                file = "index.md"

            with open(os.path.join(filepath, file), "w") as file:
                file.write(content)

print("Markdown files processed and images copied successfully.")
