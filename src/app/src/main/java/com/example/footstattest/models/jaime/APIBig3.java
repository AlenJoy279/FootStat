package com.example.footstattest.models.jaime;

import retrofit2.Call;
import retrofit2.http.GET;

public interface APIBig3 {
    // https://mocki.io/v1/c306b19f-6cca-48b9-9567-5a7846da8532
    String BASE_URL = "https://mocki.io/";
    @GET("v1/c306b19f-6cca-48b9-9567-5a7846da8532")
    Call<MainResponse> getData3();;
}
