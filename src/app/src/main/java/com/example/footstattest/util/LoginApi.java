package com.example.footstattest.util;

// Helper API for logging in
public class LoginApi {

    private String username;
    private String userId;
    private static LoginApi instance;

    public static LoginApi getInstance() {
        if (instance == null)
            instance = new LoginApi();
        return instance;

    }

    public LoginApi(){}


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
