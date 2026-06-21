import { useEffect, useState } from "react";
import axios from "axios";

function ReportCard() {

  const [report, setReport] =
    useState("");

  useEffect(() => {

    axios.get(
      "http://127.0.0.1:5000/api/ai-report"
    )
    .then(res => {

      setReport(
        res.data
      );

    })
    .catch(console.error);

  }, []);

  return (

    <div
      style={{
        padding: "20px",
        margin: "20px",
        border: "1px solid #ccc"
      }}
    >

      <h2>
        AI Intelligence Report
      </h2>

      <pre
        style={{
          whiteSpace:
          "pre-wrap"
        }}
      >
        {report}
      </pre>

    </div>
  );
}

export default ReportCard;