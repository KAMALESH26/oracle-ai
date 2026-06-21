import api from "./api";

export const getTrends = async () => {

    const response = await api.get(
        "/api/trends"
    );

    return response.data;
};