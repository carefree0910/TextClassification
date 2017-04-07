from Util.Bases import ClassifierBase
from Util.Metas import SKCompatibleMeta

import sklearn.naive_bayes as nb
from sklearn.svm import SVC, LinearSVC


class SKMultinomialNB(nb.MultinomialNB, ClassifierBase, metaclass=SKCompatibleMeta):
    pass


class SKGaussianNB(nb.GaussianNB, ClassifierBase, metaclass=SKCompatibleMeta):
    pass


class SKLinearSVM(LinearSVC, ClassifierBase, metaclass=SKCompatibleMeta):
    pass


class SKSVM(SVC, ClassifierBase, metaclass=SKCompatibleMeta):
    pass
