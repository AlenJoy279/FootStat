package com.example.footstattest.models.jaime;

import retrofit2.Call;
import retrofit2.http.GET;

public interface APICallBundesliga {
    //https://mocki.io/v1/22eb1615-9bef-490d-a26a-0273cd4d6375
    String BASE_URL = "https://mocki.io/";
    @GET("v1/22eb1615-9bef-490d-a26a-0273cd4d6375")
    Call<MainResponse> getData1();
}
