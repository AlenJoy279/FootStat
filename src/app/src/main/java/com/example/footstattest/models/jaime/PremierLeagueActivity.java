package com.example.footstattest.models.jaime;

import android.os.Bundle;
import android.util.Log;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;

import com.example.footstattest.R;
import com.example.footstattest.models.TeamListAdapter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class PremierLeagueActivity extends AppCompatActivity {
    List<Standing> dataList;
    public static final String TAG = "Premier";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_premier_league);
        ListView premier = (ListView) findViewById(R.id.premier_list);
        ArrayList<Table> tableList = new ArrayList<>();



        // Retrofit Builder
        Retrofit retrofit = new Retrofit.Builder().baseUrl(APICall.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        // instance for interface
        APICall APICall = retrofit.create(APICall.class);

        Call<MainResponse>call = APICall.getData();

        call.enqueue(new Callback<MainResponse>() {
            @Override
            public void onResponse(Call<MainResponse> call, Response<MainResponse> response) {
                MainResponse mainResponse = response.body();

                //PutDataIntoRecyclerView(Arrays.asList(mainResponse.getStandings()));


                dataList = new ArrayList(Arrays.asList(mainResponse.getStandings()));

                dataList = mainResponse.getStandings();

                for (int i = 0; i < dataList.get(0).getTable().size(); i++) {

                    Table printFormat = new Table();
                    printFormat.setName(dataList.get(0).getTable().get(i).getTeam().getName());
                    printFormat.setPosition(dataList.get(0).getTable().get(i).getPosition());
                    printFormat.setWon(dataList.get(0).getTable().get(i).getWon());
                    printFormat.setDraw(dataList.get(0).getTable().get(i).getDraw());
                    printFormat.setLost(dataList.get(0).getTable().get(i).getLost());
                    Log.d(TAG, "onResponse: " + printFormat.getName());
                    tableList.add(printFormat);


                }
                Log.d(TAG, "onResponse: " + tableList.size());


                TeamListAdapter adapterA = new TeamListAdapter(PremierLeagueActivity.this, R.layout.league_row, tableList);
                premier.setAdapter(adapterA);
            }

            @Override
            public void onFailure(Call<MainResponse> call, Throwable t) {
            }
        });
    }
}