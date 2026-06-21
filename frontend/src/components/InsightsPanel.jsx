function InsightsPanel() {

  const insights = [

    {

      title:
      "Top Emerging Trend",

      value:
      "OpenAI"
    },

    {

      title:
      "Highest Momentum",

      value:
      "Anthropic"
    },

    {

      title:
      "Prediction",

      value:
      "AI Infrastructure Growth"
    }

  ];

  return (

    <div>

      <h2>
        AI Insights
      </h2>

      <div
        style={{

          display:"grid",

          gridTemplateColumns:
          "repeat(3,1fr)",

          gap:"20px"
        }}
      >

        {
          insights.map(
            (
              item,
              index
            ) => (

              <div

                key={index}

                style={{

                  background:
                  "#111827",

                  padding:"20px",

                  borderRadius:"12px"
                }}
              >

                <h4>
                  {item.title}
                </h4>

                <h2>
                  {item.value}
                </h2>

              </div>

            )
          )
        }

      </div>

    </div>
  );
}

export default InsightsPanel;