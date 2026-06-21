import { useEffect, useState } from "react";
import axios from "axios";

function TopicForecastCards() {

  const [topics, setTopics] =
    useState([]);

  useEffect(() => {

    axios
      .get(
        "http://127.0.0.1:5000/api/topic-forecast"
      )
      .then((res) => {

        setTopics(
          res.data
        );

      });

  }, []);

  return (

    <div>

      <h2>
        Topic Forecasts
      </h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",
          gap: "20px",
          marginBottom: "30px"
        }}
      >

        {topics.map((topic,index) => (

          <div
            key={index}
            style={{
              background:"#111827",
              padding:"20px",
              borderRadius:"12px"
            }}
          >

            <h3>
              {topic.topic}
            </h3>

            <p>
              Current:
              {" "}
              {topic.current}
            </p>

            <p>
              Predicted:
              {" "}
              {topic.predicted}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}

export default TopicForecastCards;