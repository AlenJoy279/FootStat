package com.example.footstattest.models.jaime;

import java.io.IOException;

import okhttp3.Interceptor;
import okhttp3.Request;
import okhttp3.Response;

public class MyInterceptor {
    public Response intercept(Interceptor.Chain chain) throws IOException {
        Request request = chain.request()
                .newBuilder()
                .addHeader("X-Auth-Token", "93713de653e1499e8fff4ad3fe7fd9a4")
                .build();
        Response response = chain.proceed(request);
        return response;
    }
}
