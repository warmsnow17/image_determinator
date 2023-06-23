from django.shortcuts import render
from .forms import ImageUploadForm
from .image_determinator import image_determinator


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            width, height, result = image_determinator(image.image.path)

            image.result = result
            image.save()

            context = {
                'form': form,
                'width': width,
                'height': height,
                'classification': result,
            }
        else:
            context = {'form': form}
    else:
        form = ImageUploadForm()
        context = {'form': form}

    return render(request, 'image_determinator/upload_and_result.html', context)
