package com.example.footstattest.models.jaime;

import retrofit2.Call;
import retrofit2.http.GET;

public interface APICallLaLiga {

    // https://mocki.io/v1/7884d290-b02e-447c-8801-ec8b9ec49590
    String BASE_URL = "https://mocki.io/";
    @GET("v1/7884d290-b02e-447c-8801-ec8b9ec49590")
    Call<MainResponse> getData2();

}
