from bertopic import BERTopic


model = BERTopic(
    verbose=True
)


def detect_topics(documents):

    topics, probs = model.fit_transform(
        documents
    )

    return (
        topics,
        probs,
        model
    )