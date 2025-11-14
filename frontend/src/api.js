import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

import React, { useEffect, useState } from "react";
import { api } from "./api";

function Tours() {
  const [tours, setTours] = useState([]);

  useEffect(() => {
    api.get("/tours/").then((res) => setTours(res.data));
  }, []);

  return (
    <div>
      <h1>Tours</h1>
      {tours.map((t) => (
        <div key={t.id}>
          <h3>{t.name}</h3>
          <p>{t.location}</p>
          <p>${t.price}</p>
        </div>
      ))}
    </div>
  );
}

export default Tours;
