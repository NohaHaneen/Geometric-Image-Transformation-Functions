from Transformation.perspectiveTransformation import perspectiveTransformation
from Transformation.affineTransformation import affineTransformation
from Transformation.polarTransformation import polarTransformation
from Transformation.logPolarTransformation import logPolarTransformation
from Transformation.rotationTransformation import rotationTransformation
from Transformation.scalingTransformation import scalingTransformation
from Transformation.translationTransformation import translationTransformation

def startTransformation(param_data):
    print("startTransformation")
    transformation = param_data['transformation']
    inputImageName = param_data['inputImageName']
    parameters = param_data['parameters']
    print(transformation)
    if transformation == 'Perspective':
        return perspectiveTransformation(inputImageName,parameters)
    elif transformation == 'Affine':
        return affineTransformation(inputImageName,parameters)
    elif transformation == 'Polar':
        return polarTransformation(inputImageName,parameters)
    elif transformation == 'LogPolar':
        return logPolarTransformation(inputImageName,parameters)
    elif transformation == 'Rotation':
        return rotationTransformation(inputImageName,parameters)
    elif transformation == 'Scaling':
        return scalingTransformation(inputImageName,parameters)
    elif transformation == 'Translation':
        return translationTransformation(inputImageName,parameters)