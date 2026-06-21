function StatsCards() {

  const cards = [

    {
      title:"Articles",
      value:"1,284"
    },

    {
      title:"Trends",
      value:"82"
    },

    {
      title:"Sources",
      value:"3"
    },

    {
      title:"Predictions",
      value:"26"
    }
  ];

  return (

    <div
      style={{
        display:"grid",
        gridTemplateColumns:
          "repeat(4,1fr)",
        gap:"20px",
        marginBottom:"30px"
      }}
    >

      {
        cards.map((card,index)=>(

          <div

            key={index}

            style={{
              background:"#111827",
              padding:"20px",
              borderRadius:"12px"
            }}
          >

            <h4>
              {card.title}
            </h4>

            <h1>
              {card.value}
            </h1>

          </div>

        ))
      }

    </div>
  );
}

export default StatsCards;