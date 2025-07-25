from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class InappropriatenessClassification(AbsTaskClassification):
    superseded_by = "InappropriatenessClassification.v2"
    metadata = TaskMetadata(
        name="InappropriatenessClassification",
        dataset={
            "path": "ai-forever/inappropriateness-classification",
            "revision": "601651fdc45ef243751676e62dd7a19f491c0285",
        },
        description="Inappropriateness identification in the form of binary classification",
        reference="https://aclanthology.org/2021.bsnlp-1.4",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["rus-Cyrl"],
        main_score="accuracy",
        date=("2006-01-01", "2021-04-01"),
        domains=["Web", "Social", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="cc-by-nc-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{babakov-etal-2021-detecting,
  abstract = {Not all topics are equally {``}flammable{''} in terms of toxicity: a calm discussion of turtles or fishing less often fuels inappropriate toxic dialogues than a discussion of politics or sexual minorities. We define a set of sensitive topics that can yield inappropriate and toxic messages and describe the methodology of collecting and labelling a dataset for appropriateness. While toxicity in user-generated data is well-studied, we aim at defining a more fine-grained notion of inappropriateness. The core of inappropriateness is that it can harm the reputation of a speaker. This is different from toxicity in two respects: (i) inappropriateness is topic-related, and (ii) inappropriate message is not toxic but still unacceptable. We collect and release two datasets for Russian: a topic-labelled dataset and an appropriateness-labelled dataset. We also release pre-trained classification models trained on this data.},
  address = {Kiyv, Ukraine},
  author = {Babakov, Nikolay  and
Logacheva, Varvara  and
Kozlova, Olga  and
Semenov, Nikita  and
Panchenko, Alexander},
  booktitle = {Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing},
  editor = {Babych, Bogdan  and
Kanishcheva, Olga  and
Nakov, Preslav  and
Piskorski, Jakub  and
Pivovarova, Lidia  and
Starko, Vasyl  and
Steinberger, Josef  and
Yangarber, Roman  and
Marci{\'n}czuk, Micha{\l}  and
Pollak, Senja  and
P{\v{r}}ib{\'a}{\v{n}}, Pavel  and
Robnik-{\v{S}}ikonja, Marko},
  month = apr,
  pages = {26--36},
  publisher = {Association for Computational Linguistics},
  title = {Detecting Inappropriate Messages on Sensitive Topics that Could Harm a Company{'}s Reputation},
  url = {https://aclanthology.org/2021.bsnlp-1.4},
  year = {2021},
}
""",
        prompt="Classify the given message as either sensitive topic or not",
    )

    def dataset_transform(self):
        self.dataset = self.stratified_subsampling(
            self.dataset, seed=self.seed, n_samples=2048, splits=["test"]
        )


class InappropriatenessClassificationV2(AbsTaskClassification):
    metadata = TaskMetadata(
        name="InappropriatenessClassification.v2",
        dataset={
            "path": "mteb/inappropriateness",
            "revision": "2bdbb71d9b972709173f1477d7dd33c3d67f51ac",
        },
        description="""Inappropriateness identification in the form of binary classification
        This version corrects errors found in the original data. For details, see [pull request](https://github.com/embeddings-benchmark/mteb/pull/2900)""",
        reference="https://aclanthology.org/2021.bsnlp-1.4",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["rus-Cyrl"],
        main_score="accuracy",
        date=("2006-01-01", "2021-04-01"),
        domains=["Web", "Social", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="cc-by-nc-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{babakov-etal-2021-detecting,
  abstract = {Not all topics are equally {``}flammable{''} in terms of toxicity: a calm discussion of turtles or fishing less often fuels inappropriate toxic dialogues than a discussion of politics or sexual minorities. We define a set of sensitive topics that can yield inappropriate and toxic messages and describe the methodology of collecting and labelling a dataset for appropriateness. While toxicity in user-generated data is well-studied, we aim at defining a more fine-grained notion of inappropriateness. The core of inappropriateness is that it can harm the reputation of a speaker. This is different from toxicity in two respects: (i) inappropriateness is topic-related, and (ii) inappropriate message is not toxic but still unacceptable. We collect and release two datasets for Russian: a topic-labelled dataset and an appropriateness-labelled dataset. We also release pre-trained classification models trained on this data.},
  address = {Kiyv, Ukraine},
  author = {Babakov, Nikolay  and
Logacheva, Varvara  and
Kozlova, Olga  and
Semenov, Nikita  and
Panchenko, Alexander},
  booktitle = {Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing},
  editor = {Babych, Bogdan  and
Kanishcheva, Olga  and
Nakov, Preslav  and
Piskorski, Jakub  and
Pivovarova, Lidia  and
Starko, Vasyl  and
Steinberger, Josef  and
Yangarber, Roman  and
Marci{\'n}czuk, Micha{\l}  and
Pollak, Senja  and
P{\v{r}}ib{\'a}{\v{n}}, Pavel  and
Robnik-{\v{S}}ikonja, Marko},
  month = apr,
  pages = {26--36},
  publisher = {Association for Computational Linguistics},
  title = {Detecting Inappropriate Messages on Sensitive Topics that Could Harm a Company{'}s Reputation},
  url = {https://aclanthology.org/2021.bsnlp-1.4},
  year = {2021},
}
""",
        prompt="Classify the given message as either sensitive topic or not",
        adapted_from=["InappropriatenessClassification"],
    )

    def dataset_transform(self):
        self.dataset = self.stratified_subsampling(
            self.dataset, seed=self.seed, n_samples=2048, splits=["test"]
        )


class InappropriatenessClassificationv2(AbsTaskClassification):
    metadata = TaskMetadata(
        name="InappropriatenessClassificationv2",
        dataset={
            "path": "mteb/InappropriatenessClassificationv2",
            "revision": "698cb161a90150ec46618f714cdd8606cf21a9eb",
        },
        description="Inappropriateness identification in the form of binary classification",
        reference="https://aclanthology.org/2021.bsnlp-1.4",
        type="Classification",
        category="t2t",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["rus-Cyrl"],
        main_score="accuracy",
        date=("2006-01-01", "2021-04-01"),
        domains=["Web", "Social", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="cc-by-nc-sa-4.0",
        annotations_creators="human-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{babakov-etal-2021-detecting,
  abstract = {Not all topics are equally {``}flammable{''} in terms of toxicity: a calm discussion of turtles or fishing less often fuels inappropriate toxic dialogues than a discussion of politics or sexual minorities. We define a set of sensitive topics that can yield inappropriate and toxic messages and describe the methodology of collecting and labelling a dataset for appropriateness. While toxicity in user-generated data is well-studied, we aim at defining a more fine-grained notion of inappropriateness. The core of inappropriateness is that it can harm the reputation of a speaker. This is different from toxicity in two respects: (i) inappropriateness is topic-related, and (ii) inappropriate message is not toxic but still unacceptable. We collect and release two datasets for Russian: a topic-labelled dataset and an appropriateness-labelled dataset. We also release pre-trained classification models trained on this data.},
  address = {Kiyv, Ukraine},
  author = {Babakov, Nikolay  and
Logacheva, Varvara  and
Kozlova, Olga  and
Semenov, Nikita  and
Panchenko, Alexander},
  booktitle = {Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing},
  editor = {Babych, Bogdan  and
Kanishcheva, Olga  and
Nakov, Preslav  and
Piskorski, Jakub  and
Pivovarova, Lidia  and
Starko, Vasyl  and
Steinberger, Josef  and
Yangarber, Roman  and
Marci{\'n}czuk, Micha{\l}  and
Pollak, Senja  and
P{\v{r}}ib{\'a}{\v{n}}, Pavel  and
Robnik-{\v{S}}ikonja, Marko},
  month = apr,
  pages = {26--36},
  publisher = {Association for Computational Linguistics},
  title = {Detecting Inappropriate Messages on Sensitive Topics that Could Harm a Company{'}s Reputation},
  url = {https://aclanthology.org/2021.bsnlp-1.4},
  year = {2021},
}
""",
        prompt="Classify the given message as either sensitive topic or not",
    )
