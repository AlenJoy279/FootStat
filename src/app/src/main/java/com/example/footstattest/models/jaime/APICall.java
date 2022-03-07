package com.example.footstattest.models.jaime;

import retrofit2.Call;
import retrofit2.http.GET;


public interface APICall {

    // https://mocki.io/v1/be1f5fdc-0c5e-4502-8d71-3290a53295ee


    // v1/bc34e5d4-8fc5-4105-850e-cf5c5c2ca4e3
    // v1/b5a46910-d110-48fd-a616-6a68b1e3f898
    // v1/394d4273-b7ff-45a8-9c58-bffd19a5b4d8
    // http://api.football-data.org/v2/competitions/2021/standings
    // https://mocki.io/v1/9a578563-28ae-4d31-9908-d930352cda95

    //Call<MainResponse> @Path("api_key") String api_key;
    String BASE_URL = "https://mocki.io/";
    @GET("v1/ca624918-494b-49c3-a305-47bcc59d6fe8")
   // @Headers("X-Auth-Token : 93713de653e1499e8fff4ad3fe7fd9a4")

    Call<MainResponse> getData();


}
